---
notion_id: 355f2dcd-4912-81ff-9980-de734a7c6161
title: Responsible Retrieval Augmented Generation for Climate Decision Making from Documents
bib_key: DBLP:journals/corr/abs-2410-23902
year: 2024
domain: earth
type: Method
venue: arXiv
paper_link: https://arxiv.org/abs/2410.23902
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Responsible Retrieval Augmented Generation for Climate Decision Making from Documents

> arXiv | 2024 | Method | earth
## 📌 한 줄 요약
기후 법률·정책 문서를 대상으로 책임감 있는 RAG 시스템을 구축하고, 도메인 특화 4차원 평가 프레임워크 및 전문가 human-annotated 데이터셋을 공개한 논문.
## 🎯 연구 배경 및 동기
**기존 방법의 한계점**
- 기후 법률·정책 문서는 방대하고 기술적이며 다국어로 작성되어 핵심 정보 접근이 어려움
- 일반 LLM은 (1) 환각·오정보 생성, (2) 출력 속성 제어 어려움, (3) 특수 도메인 성능 저하 문제가 있음
- 기존 기후 RAG 앱(ChatClimate, ChatNetZero)은 엄밀한 평가가 없거나 소규모이며, UX가 LLM 생성 내용을 원문에 링크하지 않음
- 법률 도메인 LLM 연구에서 공정성·투명성·환각 평가 필요성이 명확히 제기됨
**이 연구가 필요한 이유**
- 기후 의사결정 지원은 인간 복지에 직접 영향을 미치는 고위험 AI 적용 사례
- 취약 계층과 저중소득 국가에 불균형적 영향을 주는 기후 변화 특성상 책임 있는 배포 원칙 필요
- 도메인 특화 생성 정책 가이드라인 및 강건한 평가 데이터셋 부재
## 🏗️ 시스템 아키텍처
```javascript
[사용자 입력]
    ↓
[Input Guardrails] → 악의적·문제적 쿼리 필터링 (NeMo Guardrails, red-teaming)
    ↓
[Information Retrieval] → BM25 + Dense Retrieval 하이브리드
    ↓
[Answer Synthesis] → GPT-4/GPT-4o/Llama 3.1/Gemini-1.5-pro
    ↓
[Output Guardrails + Auto-Evaluators]
    - CPR 정책 준수 평가 (Gemini-1.5-pro)
    - 충실도 평가 앙상블 (Patronus Lynx + Gemini G-Eval + Vectara)
    - 포매팅 규칙 체크
    - 응답 여부 확인
    ↓
[UX 노출] → 사용자에게 각 평가 결과 투명하게 제공
```
## 🔑 핵심 모듈 상세 설명
**1. 데이터베이스**
- Climate Policy Radar (CPR) DB: 전 세계 모든 국가 정부 발간 기후 법률·정책 6,000+ 문서
- 평가용 550개 문서 샘플링 (World Bank Regions 균등 분배, 번역 여부 층화)
- 평균 80페이지, 일부 1,000페이지 이상, 테이블·그림·레이아웃 포함 복잡 문서
- IEA, IAEA, OSCE, WMO 에너지 문서 추가 포함 (RAG 선호도 데이터셋용)
**2. Retrieval 실험**
| 방법 | 설명 |
| BM25 | 희소 검색 baseline |
| Dense (4종) | 오픈소스 dense retrieval 모델 단독 |
| Hybrid (4종) | α·BM25 + dense (α=0.2) |

- 총 173,000 pairwise LLM 판정으로 벤치마크
- Recall 최우선 지표 (LLM에 전달되는 관련 정보 비율 극대화)
**3. 평가 프레임워크 4차원**
| 차원 | 설명 | 평가 방법 |
| CPR 생성 정책 준수 | 공정성·객관성·충실성·인간 안전 위험 회피 | Gemini-1.5-pro LLM-as-judge |
| 충실도 | 제공 컨텍스트 기반 생성 (환각 감지) | Patronus Lynx + Gemini G-Eval + Vectara 앙상블 |
| 포매팅 | 마크다운 bullet-point + 인용 규칙 | regex·텍스트 규칙 기반 |
| 응답 여부 | 응답 불가 케이스 올바른 처리 | 텍스트 서치 |

**4. Human Annotation**
- UNECE 협력: 16명 도메인 전문가 (UN, IRENA, WMO, 각국 정부)
- 3주 어노테이션 스프린트: 800개 문서 대상 생성 데이터 라벨링
- 최종 데이터셋: 1,009 트리플 (query, retrieved passages, response), 정책 위반 15.6%
- HuggingFace 공개: [ClimatePolicyRadar/rag-climate-expert-eval](https://huggingface.co/datasets/ClimatePolicyRadar/rag-climate-expert-eval)
## 🧪 실험 및 평가
**Retrieval 평가 결과**
- Retrieval LLM Judge (GPT-4o 기반): F1 82.3% precision, 69.0% recall, 75.3% F1
- 194개 합성 질문 어노테이션 데이터셋 (2명 전문가 annotator, 0-2 관련도 척도)
- 패시지 랭킹 프레이밍의 한계 발견: 유용 정보 근접 신호, 비특정 언어, 문서 메타데이터 필요 케이스
**Generation 평가 결과 (CPR 정책 준수)**
| 모델 | Recall | Precision | F1 | Accuracy |
| GPT-4o | 0.987 | 0.343 | 0.509 | 0.708 |
| GPT-4 | 0.865 | 0.588 | 0.700 | 0.886 |
| Llama-3.1 | 0.487 | 0.854 | 0.620 | 0.908 |
| Gemini-1.5-pro | 0.961 | 0.542 | 0.693 | 0.869 |

- 안전 배포 관점에서 Recall 최우선 → Gemini-1.5-pro 자동 평가기 선택
- 충실도 위반 285건 중 100건(67.1%)이 정책 위반 True Positive와 중복
**충실도 평가기 앙상블**
- Vectara (NLU 기반): 다른 모델과 낮은 일치도 (다른 접근법)
- Gemini↔GPT-4o: 높은 일치도
- Patronus Lynx↔G-Eval Llama: pairwise F1 0.47 (파인튜닝이 기반 모델 대비 큰 변화)
- LLM이 자신의 생성을 선호하는 편향 확인 (self-preference bias)
- 최종: Patronus Lynx + Gemini G-Eval + Vectara 앙상블
## 💡 핵심 기여
- 기후 도메인 특화 RAG 생성 정책 및 4차원 평가 프레임워크 최초 제안
- UNECE 전문가 16인 협력 human-annotated 데이터셋 공개 (HuggingFace)
- Defense-in-depth UX 설계: 각 자동 평가 결과를 사용자에게 투명하게 노출
- 오픈소스 retrieval 모델 vs BM25 하이브리드 체계적 비교
- 라이브 데모 및 평가 하니스 공개로 기후·정책 커뮤니티 재현성 지원
## ⚠️ 한계점
- 현재 단일 문서 스코프 (멀티 문서 확장 미완)
- 소규모 정책 위반 데이터셋으로 프롬프트 튜닝 효과 충분한 검증 어려움
- 오픈소스 dense 모델이 특정 설정에서 BM25 대비 제한적 성능
- 패시지 랭킹 프레이밍 자체의 한계 (계층적·멀티홉 검색 등 대안 제안)
## 🔗 관련 연구 및 관련 정보
- **arXiv**: [https://arxiv.org/abs/2410.23902](https://arxiv.org/abs/2410.23902)
- **라이브 데모**: [https://queried.labs.climatepolicyradar.org/](https://queried.labs.climatepolicyradar.org/)
- **데이터셋**: [https://huggingface.co/datasets/ClimatePolicyRadar/rag-climate-expert-eval](https://huggingface.co/datasets/ClimatePolicyRadar/rag-climate-expert-eval)
- **어노테이션 가이드북**: [https://climatepolicyradar.notion.site/Annotation-Guidebook-for-Generative-AI-Data-Labelling](https://climatepolicyradar.notion.site/Annotation-Guidebook-for-Generative-AI-Data-Labelling)
- **관련 연구**: ChatClimate, ChatNetZero, ClimateGPT (기후 도메인 RAG 선행 연구)
