---
title: "Clinfo.ai: An Open-Source Retrieval-Augmented Large Language Model System for Answering Medical Questions using Scientific Literature"
bib_key: "DBLP:journals/corr/abs-2310-16146"
year: 2024
domain: medical
type: Method
venue: PSB (Pacific Symposium on Biocomputing)
paper_link: https://arxiv.org/abs/2310.16146
---

# Clinfo.ai: Open-Source RAG System for Medical QA over Scientific Literature
> PSB 2024 | Method | medical

## 한 줄 요약
Clinfo.ai는 임상 질문을 입력받아 PubMed(또는 Semantic Scholar)에서 과학 문헌을 동적으로 검색하고, 관련 초록만 선별·요약한 뒤 번호 인용이 달린 근거 기반 답변을 생성하는 최초의 공개 오픈소스 end-to-end retrieval-augmented LLM(RetA LLM) 시스템이다. 네 개의 LLM 모듈을 하나의 "LLM chain"으로 연결하고 외부 검색 인덱스(Entrez API)에 결합한 구조로, GPT-3.5/GPT-4의 zero-shot 추론 능력을 fine-tuning 없이 프롬프트만으로 활용한다.

## 시스템 구조 (Clinfo.ai Architecture)
Clinfo.ai는 검색 인덱스(PubMed 또는 Semantic Scholar)에 결합된 **네 개의 LLM이 협력하는 LLM chain**으로 구성된다(Figure 2). 모든 LLM 단계는 OpenAI의 GPT-3.5(`gpt-3.5-turbo-0613`)와 GPT-4(`gpt-4-0613`) 스냅샷을 사용하며, LangChain API를 통해 프롬프트를 주고받는다. 공통 설정으로 temperature 0.5, 최대 생성 토큰 1024를 사용한다. 모든 단계별 프롬프트는 보충 자료(GitHub `SupplementalMaterial`)에 공개되어 있다.

- **(1) Query Generator (Question2Query)**: 사용자가 제출한 질문을 입력받아, 관련 논문을 다수 회수할 수 있는 PubMed(또는 Semantic Scholar) 쿼리를 생성한다. 질문의 맥락과 요구를 정확히 대표하는 가장 핵심적이고 관련성 높은 키워드를 포함하도록 LLM에 지시한다. 정밀도(precision)보다 재현율(recall)을 강조하여 잠재적으로 관련 있는 논문을 최대한 많이 끌어오도록 설계된다.
- **(2) Search Index / Information Retriever (PubMed/Semantic Scholar, Entrez API)**: Query Generator가 만든 쿼리를 NCBI Entrez(E-utilities) API에 보내 PubMed 초록을 프로그램적으로 회수한다. LLM 출력이 확률적이고 쿼리마다 문헌의 다른 측면을 포착할 수 있으므로, **동일 프롬프트에 서로 다른 seed를 적용해 생성한 3개의 LLM 쿼리**가 반환한 논문의 합집합(union)을 취한다.
- **(3) Relevance Classifier (관련성 분류기)**: Query Generator가 recall을 우선하기 때문에 회수된 논문의 관련성을 판별하는 단계가 필수적이다. GPT-3.5를 사용하여 각 논문을 질문에 대해 relevant / not relevant의 **이진 분류**로 판정한다. 관련으로 판정된 논문은 전체 초록 메타데이터를 활용해 **IEEE 형식 인용**을 구성한다. 관련 논문이 35개를 초과하면 사용자가 BM25로 재정렬·필터링할 수 있다.
- **(4) Summarizer / Synthesis (요약·합성기)**: 두 개의 LLM 단계로 나뉜다. 먼저 **Summarization**은 관련으로 판정된 각 초록을 사용자 질문의 맥락 안에서 개별 요약한다. 이어 **Synthesis**는 개별 요약들을 번호가 매겨진 순서 리스트(각 번호가 하나의 인용에 대응)로 묶어 LLM에 전달하고, 간결하고 정보성 있는 종합 요약을 생성하게 한다. 이때 LLM은 **제공된 논문 요약만 사용하고 그 외 정보는 쓰지 않도록**, 그리고 인용 리스트를 통해 각 findings를 정확히 출처에 귀속하도록 지시받는다(번호 인용 grounding).

## 동작 파이프라인 (inference)
임상 질문 1건이 입력되면 다음 순서로 처리된다.

1. **질문 입력**: 사용자가 임상 질문을 WebApp에 제출한다(예: "Does high-grade dysplasia/carcinoma in situ of the biliary duct margin affect the prognosis of extrahepatic cholangiocarcinoma?").
2. **Query 생성**: Question2Query 모듈이 질문을 PubMed 쿼리로 변환한다. 동일 프롬프트·다른 seed로 3개의 쿼리를 생성한다(Figure 3에 실제 생성 쿼리 예시 표시).
3. **PubMed 검색**: Entrez API로 3개 쿼리가 반환한 초록의 합집합을 회수한다(예시 화면에서는 16개 논문 회수).
4. **관련 초록 선별**: Relevance Classifier(GPT-3.5)가 회수된 각 논문을 relevant / not relevant로 이진 분류한다. 관련 논문은 IEEE 형식 인용으로 구성되며, 35개 초과 시 BM25 재정렬 옵션이 제공된다.
5. **개별 근거 요약**: Summarization 단계에서 관련 초록 각각을 질문 맥락에 맞춰 요약한다.
6. **종합 + TL;DR 출력**: Synthesis 단계가 개별 요약을 번호 인용이 달린 **"Literature Summary"(= Synthesis)** 로 합성하고, 이를 1~2문장으로 압축한 **"TL;DR"** 도 함께 제시한다. 참고문헌은 하이퍼링크로 표시되어 사용자가 인용의 타당성과 추출된 정보를 직접 검증할 수 있다(Figure 5). 초록을 요약했더라도 최종 Literature Summary나 TL;DR에 그 논문이 포함되지 않을 수 있으나, 모든 관련 논문은 사용자에게 노출된다.

WebApp(www.clinfo.ai)은 검색 엔진(PubMed 등) 선택, 프롬프트 커스터마이징을 지원하며, 생성된 쿼리·회수 논문 수·개별 요약·최종 답변을 실시간으로 보여준다.

## 평가 방식 (중요)
태스크는 **세 단계**로 정의된다: (1) 질문으로부터 쿼리 생성·논문 회수, (2) 회수 논문의 관련성 판정, (3) 관련 논문의 findings 요약.

- **Retrieval(2단계)에만 precision/recall 적용**: RET(D,k)를 관련으로 판정해 회수한 k개 문서 집합, REL(D,q)를 SR이 참조한 문서 집합으로 두고, precision = |RET∩REL|/|RET|, recall = |RET∩REL|/|REL|로 정의한다. **요약 품질 평가에는 precision/recall을 쓰지 않는다.**
- **Summarization(3단계)은 요약 품질 지표로 평가**: Source-Augmented(SA) 지표는 UniEval(T5-large), COMET(XLM-RoBERTa), CTC Summary Consistency(BERT)를 사용하며, SR의 introduction·results·conclusion을 연결한 context를 추가로 참조한다. Source-Free(SF) 지표는 BERTScore, ROUGE-L, METEOR, chrF, GoogleBLEU, CTC Summary(context 미제공), CharacTer를 사용해 사람이 큐레이션한 정답 요약과 비교한다. UniEval은 Coherence / Consistency / Fluency / Relevance 4개 차원과 그 평균(Overall)을 측정한다.
- **세 가지 평가 regime**: 새 발견이 추후 출판되어 답이 바뀔 가능성을 통제하기 위해 — **Restricted Search(RS)**: 출판 하루 전까지의 논문만 회수 허용 / **Source Dropped(SD)**: 출판 전후 논문 모두 회수하되 출처 SR 자체는 관련 집합에서 제거 / **Unrestricted Search(US)**: 제한 없음(출처 SR 포함 가능, Elicit·Statpearls 등 폐쇄형 도구가 사실상 이 regime). SD에서 0건이 되는 질문을 모든 regime에서 제외해 146개 질문(시간 비제약)으로 비교했다.
- **검증된 수치(UniEval Overall, Unrestricted Search 기준)**: Clinfo.ai TL;DR = 0.88, Synthesis & TL;DR = 0.84, Synthesis = 0.809. 무증강 베이스라인 GPT-3.5 = 0.872, GPT-4 = 0.86. 배포 도구 Elicit = 0.713, Statpearls SS = 0.728. Clinfo.ai는 모든 출력 전략과 모든 regime에서 다른 RetA 시스템보다 UniEval Overall이 높았으며, 그 향상폭은 **최소 6.2%에서 최대 14.9%**로 보고된다.
- **Retrieval precision/recall(Table 3)**: Restricted Search precision 0.224 / recall 0.057, Source Dropped precision 0.186 / recall 0.064, Unrestricted Search precision 0.162 / recall 0.052(출처 SR이 96.5% 질문에서 회수됨, Source Included 0.965). precision은 회수 가능 문서가 제한된 Restricted Search에서 가장 높았다. (전반적으로 RetA 추가는 자동 지표상 LLM 대비 소폭 향상을 줌.)

## 함께 제안한 벤치마크: PubMedRS-200
PubMedRS-200(PubMed Retrieval and Synthesis)은 체계적 문헌고찰(systematic review, SR) 200건을 토대로 만든 공개 Open-QA 데이터셋이다. SR을 의학적 관심 질의의 대용(proxy)으로 삼아, 제목이 질문 형태인 SR에서 질문을 추출하고, 두 명의 인간 평가자가 results/conclusions에서 정답을 도출했다. 각 항목은 질문·정답·참고문헌(PubMed ID)·context 등을 포함한다. (자세한 구축 절차는 본 요약에서 생략.)

## 한계점
- **인간 평가 부재**: 인간 선호와 중간~높은 상관을 보이는 자동 지표만 사용했고, RetA LLM 시스템을 직접 인간 선호로 평가하지 않았다. 향후 인간 평가로 자동 지표와의 정렬을 확인할 필요가 있다.
- **쿼리 생성의 MeSH 환각**: LLM이 PubMed 쿼리 문법·Boolean 연산자는 대체로 잘 생성하지만, **환각된(존재하지 않는) MeSH term**을 만들어 관련 연구를 누락시킬 수 있다. 쿼리 생성 단계의 신뢰성 개선이 향후 과제다(precision/recall 향상 직결).
- **자동 평가 지표의 편향**: SF 지표는 짧은 응답에 유리해 정확성·포괄성을 보장하지 않으며, 일부 SA 지표(UniEval Coherence/Relevance, COMET)는 긴 생성을 선호한다. 지표 간 불일치로 공정한 성능 평가가 어렵다.
- **평가 가정 의존성**: SA 평가는 시스템이 SR 저자가 관련으로 본 논문을 회수·합성한다는 가정에 기대므로, 이 가정이 깨지면 출력이 과도하게 페널티를 받을 수 있다.

## 관련 정보
- arXiv: https://arxiv.org/abs/2310.16146 (v1, 2023-10-24, cs.IR)
- 발표: Pacific Symposium on Biocomputing (PSB) 2024
- DBLP bib_key: `DBLP:journals/corr/abs-2310-16146`
- WebApp: https://www.clinfo.ai/
- GitHub(코드): https://github.com/som-shahlab/Clinfo.AI
- 프롬프트/보충 자료: https://github.com/som-shahlab/Clinfo.AI/tree/main/SupplementalMaterial
- 저자: Alejandro Lozano, Scott L. Fleming, Chia-Chun Chiang, Nigam Shah (Stanford University / Mayo Clinic)
