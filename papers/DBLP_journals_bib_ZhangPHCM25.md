---
notion_id: 355f2dcd-4912-8184-b91f-c14fce4ca21b
title: Rag2Mol: structure-based drug design based on RAG
bib_key: DBLP:journals/bib/ZhangPHCM25
year: 2025
domain: bio, medical, chem
type: Method
venue: Briefings in Bioinformatics (Oxford)
paper_link: https://doi.org/10.1093/bib/bbaf265
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Rag2Mol: structure-based drug design based on RAG

> Briefings in Bioinformatics (Oxford) | 2025 | Method | bio, medical, chem
## 📌 한 줄 요약
Rag2Mol은 RAG 기반 구조 중심 신약 설계(SBDD) 프레임워크로, 두 단계 검색기(Global + Molecular Retriever)로 ZINC DB에서 구매 가능한 참조 분자를 동적으로 불러와 GVP 기반 자기회귀 모델의 분자 생성을 안내하며, 합성 가능성과 결합 친화도를 동시에 개선한다.
## 🎯 연구 배경 및 동기
**기존 SBDD 방법의 한계점**
- 기존 AI SBDD 모델은 합성 가능성을 무시하여 생성 분자가 실제 합성 가능한 화학 공간 밖에 위치하는 경우가 많음
- 데이터 편향 문제: 훈련 데이터(CrossDocked2020)가 전체 단백질-리간드 복합체 공간에 비해 극히 일부
- 기존 가상 스크리닝은 AI 모델 3개(스크리닝·도킹·결합 친화도 예측)를 순차 사용 → 각 단계의 false positive가 누적되어 성공률 저하
- 생성된 분자의 광범위한 하위 검증(도킹 계산, 웻랩 실험) 과정이 복잡하고 불확실성 축적

**이 연구가 필요한 이유**
- RAG를 SBDD에 적용하면 외부 구매 가능 분자 DB(ZINC)를 동적으로 활용 → 합성 가능성 문제 해소 가능
- 단일 모델이 스크리닝·도킹·생성을 통합 → AI 모델 순차 파이프라인의 오류 누적 감소
- 두 워크플로우(G: 신규 생성, R: 유사 분자 검색)로 다양한 실세계 신약 개발 시나리오 대응 가능
## 🏗️ 시스템 아키텍처
```javascript
[입력: 단백질 포켓 3D 구조]
        ↓
┌─────────────────────────────────────┐
│  Step 1: Global Retriever            │
│  ZINC → 가상 스크리닝 + Vina 도킹   │
│  → 포켓 특이적 소분자 DB 구축        │
└─────────────────┬───────────────────┘
                  ↓
┌─────────────────────────────────────┐
│  Step 2: 자기회귀 분자 생성 (반복)  │
│  Molecular Retriever:               │
│    포켓별 DB → 참조 분자 선택       │
│  cross-KNN 메시지 패싱 →            │
│    참조 분자 정보 → fragment에 융합  │
│  GVP 기반 모델: 다음 원자 예측      │
└─────────────────┬───────────────────┘
                  ↓
    ┌─────────────┴─────────────┐
    ↓                           ↓
[Rag2Mol-G]              [Rag2Mol-R]
생성 분자 직접 사용       생성 분자 클러스터링
                          scaffold 선택
                          ZINC 유사도 검색
                          → 구매 가능 분자 출력
                  ↓
┌─────────────────────────────────────┐
│  Step 3: 필터링 + 검증              │
│  Vina/QED/SA/Lipinski/LogP 기준     │
│  → Vina 도킹 재계산 → 웻랩 실험    │
└─────────────────────────────────────┘
```
## 🔑 핵심 모듈 상세 설명
### 1. Global Retriever (포켓 특이적 DB 구축)
- 입력: 단백질 포켓 3D 좌표
- ZINC에서 가상 스크리닝 모델로 결합 가능성 있는 소분자 1차 필터링
- AutoDock Vina로 필터링된 분자를 포켓에 도킹 → 결합 친화도 + 합성 가능성 동시 고려
- 결과: 포켓별 소분자 DB (결합 가능 + 구매 가능 분자 집합)

### 2. Molecular Retriever (참조 분자 선택)
- 분자 생성 각 단계에서 현재 생성된 fragment와 포켓별 DB의 분자들을 비교
- cross-KNN 그래프로 가장 관련성 높은 참조 분자 선택
- 참조 분자의 구조 정보를 hidden space에서 메시지 패싱으로 생성 fragment에 융합

### 3. GVP 기반 자기회귀 생성기
- E(3)-등변 GVP(Graph Vector Perceptron) 아키텍처
- 단백질 포켓 잔기 + 참조 분자를 조건으로 원자를 순차적으로 예측
- 각 스텝에서 원자 유형, 3D 좌표, 결합 유형 예측
- CrossDocked2020으로 학습 (훈련 중에도 검색기 활성)

### 4. 두 워크플로우
| 워크플로우 | 작동 방식 | 적합 상황 |
| **Rag2Mol-G** | 포켓별 DB를 참조로 신규 분자 직접 생성 | 여러 결합 템플릿이 필요한 표적, 고친화도 신규 후보 탐색 |
| **Rag2Mol-R** | 생성 분자 → 클러스터링 → scaffold → ZINC 유사도 검색 | 합성 가능한 유사체 탐색, undruggable 표적, 가상 스크리닝 대체 |

### 도구·DB 연동 테이블
| 모듈 | 사용 DB/도구 | 역할 |
| Global Retriever | ZINC (230M+ 화합물) | 구매 가능 분자 소스 |
| Global Retriever | AutoDock Vina | 도킹 점수 계산 |
| Molecular Retriever | CrossDocked2020 포켓별 DB | 훈련/추론 중 참조 분자 |
| 평가 | GNINA | CNN affinity 계산 |
| 평가 | PoseBusters | 물리적 유효성 검증 |
| 실세계 적용 | PDB (RCSB) | 표적 단백질 3D 구조 다운로드 |

## 🧪 실험 및 평가
### 평가 태스크 및 데이터셋
- **벤치마크**: CrossDocked2020 test set (100개 단백질 포켓)
- **비교 모델 (SBDD)**: Pocket2Mol, ResGen, AR, GraphBP, FLAG, TargetDiff, Pocket2MolRL, Decomp-o, Decomp-r
- **비교 모델 (가상 스크리닝, Rag2Mol-R 대비)**: ConPLex, DrugBAN, UdanDTI
- **실세계 케이스**: PTPN2 (단백질 티로신 포스파타아제, undruggable 표적, 임상 완료 억제제 없음)

### 평가 지표
| 지표 | 설명 |
| Vina Dock (kcal/mol) | 도킹 전 Vina 결합 에너지 |
| Vina Score (kcal/mol) | 재도킹 후 결합 에너지 |
| %↑ Vina | 네이티브 리간드보다 높은 Vina 점수 비율 |
| PB-Valid | PoseBusters로 검증한 물리적 유효 분자 비율 |
| CNN Affinity | GNINA 기반 CNN 결합 친화도 |
| Clash | 입체 충돌 수 |
| QED | 약물 유사성 정량 지표 |
| SA | 합성 접근성 점수 |
| Lipinski | Lipinski 규칙 5 준수 여부 |
| LogP | 지질 친화성 |

### 주요 결과
- Rag2Mol은 거의 모든 지표에서 최고 또는 근최고 성능 달성
- 특히 Vina Dock/Score top 1/3 분자가 네이티브 리간드보다 낮은(우수한) 결합 에너지 일관 달성
- Rag2Mol-R: ConPLex/DrugBAN/UdanDTI 대비 더 넓은 화학 공간 커버리지와 높은 표적 특이성
- PTPN2 케이스: 두 워크플로우 모두 유망 억제제 후보 발굴 (기존 활성 억제제 능가)
## 💡 핵심 기여
1. **RAG의 SBDD 적용**: 텍스트 RAG 패러다임을 3D 구조 기반 분자 생성으로 확장
2. **두 단계 검색기**: Global Retriever(포켓별 DB 구축) + Molecular Retriever(생성 단계별 참조 선택)로 합성 가능성 + 친화도를 동시 담보
3. **두 워크플로우**: 신규 생성(Rag2Mol-G)과 유사 분자 검색(Rag2Mol-R)으로 다양한 실용 시나리오 대응
4. **확장 가능한 프레임워크**: GVP 외 다른 SBDD 백본 모델로도 교체 가능한 모듈식 설계
5. **실세계 검증**: 미드러거블 PTPN2 표적에서 유망 억제제 발굴
## ⚠️ 한계점
- ZINC DB 품질과 커버리지에 성능 의존
- Global Retriever (가상 스크리닝 + 도킹) 계산 비용 높음
- LLM 미사용 → 자연어 기반 상호작용이나 지식 통합 불가
- 훈련 데이터 CrossDocked2020의 bias 내재 (PDB에서 이미 알려진 리간드-포켓 쌍 중심)
- Rag2Mol-R의 유사도 검색이 Morgan fingerprint 기반 → 3D 구조적 유사성 반영 한계
## 🔗 관련 연구 및 관련 정보
- **논문 링크**: [https://doi.org/10.1093/bib/bbaf265](https://doi.org/10.1093/bib/bbaf265)
- **RECOMB 2025 버전**: [https://doi.org/10.1007/978-3-031-90252-9_15](https://doi.org/10.1007/978-3-031-90252-9_15)
- **GitHub**: [https://github.com/CQ-zhang-2016/Rag2Mol](https://github.com/CQ-zhang-2016/Rag2Mol)
- **주요 베이스라인**: Pocket2Mol (ICML 2022), TargetDiff (ICLR 2023), ResGen (Nature Machine Intelligence 2023)
- **유사 방법론**: PocketCrafter (Novartis, Shen et al. 2024), FLAG (ICLR 2023)
- **사용 데이터셋**: CrossDocked2020 (Francoeur et al., J. Chem. Inf. Model. 2020)
