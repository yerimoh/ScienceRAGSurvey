---
notion_id: 355f2dcd-4912-81ca-94c7-d04120963836
title: Three-Dimensional Convolutional Neural Networks and a Cross-Docked Data Set for Structure-Based Drug Design
bib_key: DBLP:journals/jcisd/FrancoeurMSJISK20
year: 2020
domain: bio, medical, chem
type: benchmark
venue: J. Chem. Inf. Model.
paper_link: https://doi.org/10.1021/acs.jcim.0c00411
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Three-Dimensional Convolutional Neural Networks and a Cross-Docked Data Set for Structure-Based Drug Design

> J. Chem. Inf. Model. (ACS) | 2020 | Benchmark | bio, medical, chem

## 한 줄 요약
CrossDocked2020은 PDB의 단백질-리간드 복합체를 cross-docking한 22.5백만 개 포즈로 구성된 구조 기반 신약 설계(SBDD) ML 벤치마크로, 단백질-리간드 결합 친화도 예측 및 SBDD 생성 모델 평가의 실질적 표준으로 자리잡았다.

## 제작 배경
**기존 벤치마크의 한계**
- PDBbind 기반 접근이 주류: 동일 리간드를 동일 구조에 다시 도킹(re-docking)하는 방식에 중점 → 실제 drug discovery의 확장성에 대한 평가가 과도하게 낙관적
- ML 모델 비교가 방법론에 따른 개별 데이터셋 사용으로 알고리즘 품질 파악 불가
- 주어진 표적에 대해 새로운 리간드를 예측하는 일반화 능력(non-cognate) 평가가 부재

**이 벤치마크가 필요한 이유**
- Cross-docking (비공유 리간드-포켓 쌍) 포즈 데이터를 대규모로 제공하여 실제 drug discovery 조건에 가까운 평가 가능
- 클러스터 기반 분할로 더 엄격하고 공정한 일반화 평가 지원
- 표준화된 train/val/test 분할 + 여러 스플릿 방법 제공으로 방법론 간 공정 비교 가능
- SBDD 생성 모델 (Pocket2Mol, TargetDiff, ResGen 등)의 사실상 표준 학습·평가 데이터셋으로 정착

## 어떻게 만들었나 (Construction Methodology)
**Step 1 — 데이터 출처 선정**
- PDB(Protein Data Bank)에서 실험적으로 결정된 단백질-리간드 복합체 구조 수집
- Pocketome DB의 유사 포켓 클러스터 정보 활용
- 전처리: 각 포켓을 ProBiS z-score 3.5 기준으로 클러스터링

**Step 2 — 구축 파이프라인 (Cross-docking)**
```
PDB 단백질-리간드 복합체 수집
    ↓
유사 포켓 클러스터링 (ProBiS 알고리즘, z-score 3.5)
    ↓
동일 클러스터 내 리간드 ↔ 비공유 포켓 cross-docking
(AutoDock Vina / Gnina)
    ↓
포즈 필터링 (RMSD, 결합 에너지 기준)
    ↓
Counter-example 생성 (반례: 잘못된 포즈 추가)
    ↓
22.5M 포즈 데이터셋 완성
```

- 리간드가 자신의 원래 포켓(cognate)이 아닌 유사 포켓(non-cognate)에도 도킹 → 더 현실적인 virtual screening 시나리오
- Counter-example(반례) 포즈를 반복적 학습 세트 구성으로 추가 → 모델 강건성 향상

**Step 3 — 품질 검증**
- 알려진 CNN 모델(Def2018 등)로 결합 친화도 예측 및 포즈 선택 성능 평가
- PDBbind Core/General 세트 대비 교차 검증으로 데이터 품질 확인
- 리간드 전용(단백질 구조 제외) 모델 평가로 인위적 bias 정량화

**Step 4 — 데이터셋 구성 및 공개**
- 전체: 22.5M 포즈 (13,780 유일 리간드, 2,922 포켓, 18,450 복합체)
- 결합 친화도 데이터 포함 비율: 41.9%
- 분할: 클러스터 기반 교차 검증 분할 제공
- Pocket2Mol 등 후속 논문에서 사용하는 전처리 서브셋: 훈련 ~100,000 복합체, 테스트 100 포켓
- GitHub (gnina/models)에 데이터, 모델 가중치, 코드 공개

## Input (입력)
입력 형식: 단백질 3D 구조 (PDB 좌표) + 리간드 SMILES/3D 좌표

| 구성요소 | 내용 | 규모 |
|---|---|---|
| 총 포즈 | Cross-docked 단백질-리간드 포즈 | 22,584,102개 |
| 유일 리간드 | 유일 소분자 리간드 | 13,780개 |
| 포켓 | 단백질 결합 포켓 | 2,922개 |
| 복합체 | 포켓-리간드 쌍 | 18,450개 |
| 결합 친화도 데이터 | 실험 친화도 포함 복합체 비율 | 41.9% |
| 반례(counter-examples) | 잘못된 포즈 (이터레이티브 학습용) | 11,892,173개 |

**제공 필드**
| 필드명 | 설명 |
|---|---|
| 단백질 PDB 파일 | 수용체 3D 좌표 |
| 리간드 SDF/mol2 | 리간드 3D 포즈 좌표 |
| Vina 점수 | 도킹 결합 에너지 (kcal/mol) |
| RMSD | 결정 구조 대비 포즈 편차 |
| 결합 친화도 (pKi/pKd) | 실험값 (포함 시) |
| 클러스터 ID | 유사 포켓 클러스터 소속 |

## Output (평가 형식)
**원 논문 평가 태스크 (CNN 모델 평가)**
- 결합 친화도 예측: RMSE, Pearson R
- 결합 포즈 분류 (맞는 포즈 vs. 반례): AUC
- 포즈 선택 정확도: 최저 RMSD 포즈 선택 정확도

**SBDD 생성 모델 평가 (후속 논문 기준)**
- Vina Dock / Vina Score: 결합 에너지 (낮을수록 좋음)
- %↑ Vina: 네이티브 리간드 대비 우월 비율
- QED: 약물 유사성
- SA: 합성 접근성
- Lipinski 규칙 5 준수
- LogP: 지질 친화성
- PB-Valid (PoseBusters): 물리적 유효성
- CNN Affinity (GNINA): CNN 기반 결합 친화도

## 예시 문항 (SBDD 태스크 유형별)
**결합 친화도 예측 예시**
- Q: 단백질 포켓 3D 좌표 + 도킹된 리간드 3D 포즈가 주어졌을 때, 이 복합체의 결합 친화도(pKd)를 예측하라.
- A: pKd ≈ 7.2 (IC50 ≈ 63 nM 수준) | 근거: 실험 측정값

**포즈 선택 예시**
- Q: 동일 리간드의 5개 도킹 포즈 중 결정 구조에 가장 가까운 포즈를 선택하라 (RMSD < 2Å).
- A: 포즈 3번 (RMSD = 1.43Å) | 근거: CNN affinity score 기반

**SBDD 생성 평가 예시 (Pocket2Mol, Rag2Mol 등)**
- Q: 단백질 포켓 3D 구조가 주어졌을 때, 결합 친화도 높고 drug-likeness 우수한 소분자를 생성하라.
- A: 평가: Vina Dock < -8.0 kcal/mol, QED > 0.5, SA > 0.5, Lipinski 준수 여부 확인

## 주요 평가 결과 (원 논문)
**CNN 모델 성능 (CrossDocked2020 test)**
| 모델 | 과제 | 성능 |
|---|---|---|
| Dense CNN (5개 앙상블) | 친화도 예측 (RMSE) | 1.42 |
| Dense CNN (5개 앙상블) | 친화도 예측 (Pearson R) | 0.612 |
| Dense CNN (5개 앙상블) | 포즈 분류 (AUC) | 0.956 |
| Dense CNN (5개 앙상블) | 포즈 선택 정확도 | 68.4% |

**SBDD 생성 모델 성능 (Rag2Mol 논문 기준)**
| 모델 | Vina Dock | QED | SA | 비고 |
|---|---|---|---|---|
| AR | 기준선 | 기준선 | 기준선 | 자기회귀 |
| Pocket2Mol | 개선 | 개선 | 개선 | 자기회귀 + 그래프 |
| TargetDiff | 개선 | 참고 | 참고 | 확산 기반 |
| **Rag2Mol** | **최고 수준** | **최고 수준** | **개선** | RAG 기반 |

## 한계점
- PDB 데이터 편향 내재: 이미 알려진 리간드-포켓 쌍 중심 → 화학 공간 전체 미커버
- Cross-docking 포즈의 실험 구조 대비 낮은 정확도
- 결합 친화도 데이터가 전체의 41.9%에만 포함 (나머지는 레이블 없음)
- 단백질 유연성 미고려 (rigid receptor docking)
- 도킹 소프트웨어(Vina/Gnina)의 scoring function bias 내재

## 관련 정보
- **논문 링크**: [https://doi.org/10.1021/acs.jcim.0c00411](https://doi.org/10.1021/acs.jcim.0c00411)
- **GitHub (gnina/models)**: [https://github.com/gnina/models](https://github.com/gnina/models)
- **이 벤치마크를 사용한 논문**: Pocket2Mol (ICML 2022), TargetDiff (ICLR 2023), ResGen (Nature MI 2023), FLAG (ICLR 2023), Rag2Mol (Briefings in Bioinformatics 2025)
