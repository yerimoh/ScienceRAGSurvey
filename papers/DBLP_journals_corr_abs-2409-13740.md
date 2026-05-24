---
notion_id: 355f2dcd-4912-8151-ac54-f3cf4d24cf83
title: Language Agents Achieve Superhuman Synthesis of Scientific Knowledge
bib_key: DBLP:journals/corr/abs-2409-13740
year: 2024
domain: bio
type: Method
venue: arXiv
paper_link: https://arxiv.org/abs/2409.13740
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Language Agents Achieve Superhuman Synthesis of Scientific Knowledge

> arXiv | 2024 | Method | bio

## 한 줄 요약
PaperQA2는 과학 문헌 검색·요약·모순탐지 세 가지 실제 태스크에서 제한 없는 인간 전문가(PhD/박사과정)를 초과하는 성능을 달성한 최초의 RAG 에이전트 시스템이다.

---
## 연구 배경 및 동기
**기존 방법의 한계**
- LLM은 hallucination(잘못된 정보를 자신 있게 생성) 문제가 있어 과학적 정확성 요구 충족 어려움
- 기존 과학문헌 벤치마크(PubMedQA, BioASQ 등)는 초록만 사용하거나 고정 코퍼스를 사용해 실제 연구 환경을 반영하지 못함
- 기존 벤치마크 대부분이 인간 성능과 직접 비교하지 않아 실용적 가치 불분명
- 단순 RAG(Perplexity, Elicit 등)는 검색 청크를 변환 없이 컨텍스트에 주입하여 distracting context 문제 발생

**이 연구가 필요한 이유**
- 과학 연구에서 문헌 검색·요약·모순탐지를 자동화하면 연구자 생산성 획기적 향상 가능
- 문헌 폭증으로 인간이 전체 문헌을 일일이 확인하는 것이 불가능해져 AI 기반 자동 탐지 시스템 필요
- 특히 모순 탐지는 "many vs many" 문제로 인간에게 실현 불가능한 규모에서 동작 가능

---
## 시스템 아키텍처
[image: PaperQA2 architecture]

```
[사용자 쿼리]
     ↓
[PaperQA2 Agent (GPT-4-Turbo, ReAct 패턴)]
     ├── Paper Search Tool
     │     키워드+연도범위 생성 → Semantic Scholar API 검색
     │     → Grobid/PyMuPDF 파싱 → Hybrid 임베딩 (dense+sparse)
     │     → 청크 저장 (agent state)
     │
     ├── Citation Traversal Tool  ← NEW
     │     RCS 점수 ≥ 8인 논문의 인용/피인용 1hop 탐색
     │     → overlap fraction 필터링 → 최대 12편 추가
     │
     ├── Gather Evidence Tool
     │     top-k (기본 30) cosine 유사도 검색
     │     → RCS: 각 청크에 LLM completion
     │         → 요약(200~400토큰) + 관련성점수(0~10)
     │     → 점수 기반 재순위화 → 상위 summaries 저장
     │
     └── Generate Answer Tool
           상위 N개(기본 15) summaries → LLM 최종 답변 생성
           → cited Wikipedia-style 답변 출력
```

**WikiCrow** (요약 특화): 유전자명 → 구조/기능/상호작용/임상의의 각 섹션별 PaperQA2 호출 4회 + overview LLM 1회 → Python으로 합성

**ContraCrow** (모순탐지 특화): 논문 청크 분할 → LLM 클레임 추출 → 품질 필터링(≥8/10) → PaperQA2로 각 클레임에 모순탐지 쿼리 → 11점 Likert 스코어 출력

---
## 핵심 모듈 상세 설명
### RCS (Reranking & Contextual Summarization)
| 항목 | 내용 |
|---|---|
| 입력 | top-k 청크 (기본 30개) |
| 처리 | 각 청크에 LLM completion: 요약 + 관련성점수(0~10) JSON 출력 |
| 출력 | 점수순 재정렬된 contextual summaries |
| 특징 | 병렬 처리로 고효율; 소스 메타데이터(인용수·저널명) 포함 주입 |
| 효과 | No RCS 대비 accuracy 유의미하게 향상 (t=9.29, p<0.001) |

### Citation Traversal Tool
| 항목 | 내용 |
|---|---|
| 기원 | RCS 점수 ≥ 8 논문에서 출발 |
| 방향 | 전방(future citers) + 후방(past references) 모두 |
| API | Semantic Scholar + Crossref |
| 필터 | overlap fraction α=1/3: 여러 소스논문이 공통 인용하는 논문만 유지 |
| 한도 | 최대 12편/호출 |
| 효과 | DOI recall 유의미하게 향상 (t=3.4, p=0.022) |

### 도구·DB 연동 테이블
| 도구 | 역할 | 비고 |
|---|---|---|
| Semantic Scholar API | 논문 검색 및 인용 탐색 | 기본 12편/검색 |
| Crossref API | 과거 참고문헌 탐색 | Semantic Scholar 보완 |
| Grobid | 섹션·표·인용 파싱 | WikiCrow에 필수; 토큰 44% 절감 |
| PyMuPDF | 기본 PDF 파싱 | LitQA2 실험 기본값 |
| OpenAI Embeddings | 임베딩 생성 | text-embedding-3-large |

---
## 실험 및 평가
### 평가 태스크 및 데이터셋
| 태스크 | 벤치마크 | 규모 | 비교 대상 |
|---|---|---|---|
| 문헌 QA | LitQA2 (자체 제작) | 248문항 (MCQ) | 인간 전문가 9명 |
| 과학 요약 | WikiCrow vs Wikipedia | 240 유전자 기사, 375 문장 평가 | 인간 작성 Wikipedia |
| 모순 탐지 | ContraDetect (자체 제작) | 93 생물학 논문, 3,180 클레임 | 전문가 5명 검증 |

### 주요 결과
| 시스템 | Precision |
|---|---|
| **PaperQA2** | **85.2%** |
| 인간 전문가 | 73.8% |
| Perplexity Pro | 69.7% |
| GPT-4-Turbo (직접) | 43.6% |
| Claude-Opus (직접) | 23.6% |

| 시스템 | Precision (인용·지지 비율) |
|---|---|
| **WikiCrow** | **86.1%** |
| Wikipedia | 71.2% |

| 지표 | 수치 |
|---|---|
| 논문당 평균 클레임 수 | 35.16 ± 21.72 |
| 논문당 탐지 모순 수 | 2.34 ± 1.99 |
| 전문가 검증 모순 수 | 1.64/논문 (하한) |
| ContraDetect AUC | 0.842 |
| ContraDetect Precision | 88% |

---
## 핵심 기여
- **인간 초과 성능 최초 달성**: 제한 없는 인간 전문가 대비 LitQA2 precision 유의미하게 초과 (p=0.0036)
- **RCS 기법**: top-k 검색 후 LLM으로 각 청크를 요약+점수화하여 노이즈 청크 제거 → precision 대폭 향상
- **Citation Traversal 도구**: 인용 그래프를 계층적 인덱싱으로 활용 → recall 유의미하게 향상
- **WikiCrow**: 인간 작성 Wikipedia보다 정확한 유전자 기사 자동 생성 (reasoning error 12 vs 26개)
- **ContraCrow**: 생물학 문헌에서 논문당 평균 1.64개의 검증 가능 모순 자동 탐지
- **엄격한 인간 비교 방법론**: 인터넷·도구 완전 허용 상태의 PhD 전문가와 동일 조건 비교

---
## 한계점
- **폐쇄 접근 논문 누락**: 라이선스 제약으로 오픈액세스 논문만 사용 가능 → 중요 결과 누락 가능성
- **ContraCrow 오버컨피던스**: 인간 간 일치율 75.5% vs ContraCrow-인간 일치율 60.4% → 과도한 확신 경향
- **비용**: 쿼리당 $1~3, WikiCrow 기사당 $4.48 → 대규모 배포 시 비용 부담
- **소형 모델 성능 저하**: RCS에 Llama3-70B, GPT-3.5-Turbo 사용 시 accuracy 오히려 감소 → 고성능 LLM 의존
- **추상적 추론 한계**: LLM 자체의 추론 오류(hallucination) 여전히 존재 (WikiCrow reasoning issue 12개)

---
## 관련 연구 및 관련 정보
- **원 논문**: [https://arxiv.org/abs/2409.13740](https://arxiv.org/abs/2409.13740)
- **GitHub**: [https://github.com/Future-House/paper-qa](https://github.com/Future-House/paper-qa) (paperqa 오픈소스)
- **WikiCrow 생성 기사**: [https://storage.googleapis.com/fh-public/wikicrow2/](https://storage.googleapis.com/fh-public/wikicrow2/)
- **선행 연구**: PaperQA (arXiv 2312.07559), Lab-bench (arXiv 2407.10362)
- **이 논문이 제작한 벤치마크**: LitQA2 (248 MCQ), ContraDetect
