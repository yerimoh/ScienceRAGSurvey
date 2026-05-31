---
title: "BioReader: a Retrieval-Enhanced Text-to-Text Transformer for Biomedical Literature"
bib_key: "DBLP:conf/emnlp/FrisoniMMV22"
year: 2022
domain: bio, medical
type: Method
venue: EMNLP
paper_link: https://aclanthology.org/2022.emnlp-main.390/
---
# BioReader: Retrieval-Enhanced T5 for Biomedical Literature
> EMNLP 2022 | Method | bio · medical

## 한 줄 요약
BioReader는 생의학 문헌을 위한 최초의 retrieval-enhanced text-to-text 모델로, T5 백본에 RETRO의 chunked cross-attention을 이식하고 frozen CONTRIEVER 검색기로 PubMed 기반 외부 데이터스토어(약 6,000만 토큰)에서 관련 문헌 청크를 실시간으로 가져와 입력을 보강한다. 모든 생의학 NLP 태스크를 "외부 지식의 도움을 받아 텍스트를 변환하는" 문제로 캐스팅하며, 최대 3배 적은 파라미터로 여러 SOTA를 능가한다.

## 시스템 구조 (BioReader Architecture)
**백본 (T5 + RETRO-blocks).** BioReader는 T5 encoder–decoder를 확장한 모델이다. GPT 기반의 RETRO와 달리 원래 T5 skeleton을 유지하며, decoder에서 RETRO-block과 표준 T5-block을 번갈아 배치한다.
- T5 encoder는 그대로 유지한다.
- RETRO-block은 fully-connected(FFW), self-attention(ATT), chunked cross-attention(CCA)를 조합한다: `RETRO(H,E) = FFW(CCA(ATT(H), E))`, 표준 블록은 `T5(H) = FFW(ATT(H))`.
- T5-base(12층, d=768)에서 9·12번째 층에 RETRO-block을 둔다(P={9,12}). 이 지점에서 neighbor encoding과 입력 encoding이 CCA로 병합되어 encoder 출력을 대체한다.
- 최종 구성은 229.5M 파라미터.

**Neural retrieval DB (Evidence Datastore).** 학습 코퍼스와 다른 검색 풀을 쓴다(도메인 적응·지식 갱신에 유리). 데이터스토어는 PubMed-RCT에서 유도된 무작위 대조시험(RCT) 영문 초록 약 200K개로 구성되며, 전체적으로 PubMed 중심 약 6,000만 토큰 규모다. 각 value는 인접한 두 청크 [N, F](neighbor + 원본 초록에서의 연속)로 구성되고, key는 미리 계산된 f(N)이다.

**검색기 (Retriever).** 매핑 함수 f(·)는 frozen, bi-directional encoder인 CONTRIEVER(BERT-base 기반 dual-encoder, MoCo contrastive로 unsupervised 학습)로 구현되며, 마지막 층 출력에 average pooling을 적용한다.

**Chunked Cross-Attention (CCA) — neighbor 융합.** 출력 확률을 보간하거나 입력을 단순 concat하는 방식과 달리, BioReader는 입력 프롬프트와 neighbor를 따로 인코딩한 뒤 CCA로 조립한다.
- 입력을 크기 m=16의 청크로 분할(n=512)하고, 각 청크 C_u에 대해 dot product로 top-k 문서를 FAISS로 검색한다.
- 검색된 [N, F]는 각각 길이 16 → neighbor 토큰은 k×32 형태로 T5-encoder가 인코딩한다.
- 각 입력 청크는 직전(preceding) 청크의 neighbor에만 attend하며, one-token overlap으로 autoregression이 보장된다.

## 동작 파이프라인 (inference)
1. **입력 분할:** 입력을 크기 16의 청크로 나눈다(n=512).
2. **검색:** 각 청크를 frozen CONTRIEVER로 인코딩하고 FAISS로 데이터스토어에서 top-k 검색 → neighbor + continuation 획득.
3. **인코딩:** 입력 프롬프트와 검색된 neighbor를 (같은) T5 encoder로 따로 인코딩.
4. **융합:** decoder의 RETRO-block(P={9,12})에서 CCA가 입력·neighbor encoding을 병합해 encoder 출력을 대체.
5. **디코딩:** 표준 T5 greedy decoding. 첫 청크는 neighbor에 의존하지 않게 둔다. 입력에 task-specific prefix를 붙여 모든 태스크를 text-to-text로 캐스팅.

## 학습/구성 (training)
- **백본 초기화:** T5-block은 SCIFIVE(PubMed)-base 가중치로 초기화.
- **파라미터 효율:** RETRO를 따라 pre-trained 가중치를 freeze하고 새 CCA 파라미터(전체의 5% 미만)만 span-mask 학습한다. 따라서 검색 없이 평가하면 원래 SCIFIVE 성능이 유지된다. CCA 학습에는 pre-training 인스턴스의 약 3%만 사용.
- **Fine-tuning:** 이후 target task에서 전체 층을 fine-tune(teacher forcing MLE), task-specific prefix로 multi-task 학습.
- **평가:** 18개 데이터셋 6개 카테고리(NER, RE, NLI, DC, QA, OpenQA), 대부분 BLURB에서 차용.

## 주요 결과
약 3배 큰 SCIFIVE-large(770M)를 여러 태스크에서 능가(BioReader 229.5M).

**QA / OpenQA — Exact Match**

| Model | #params | BioASQ4b | BioASQ5b | BioASQ6b | MedQA-USMLE |
|---|---|---|---|---|---|
| SCIFIVE-base | 220M | 60.80 | 59.53 | 55.56 | 34.57 |
| SCIFIVE-large | 770M | 62.98 | 61.67 | 61.74 | 35.12 |
| **BioReader** | **229.5M** | **64.13** | **62.02** | **62.18** | **42.96** |

NER/RE/DC에서도 BC4CHEMD 92.81, Species-800 77.44, DDI 84.34, HoC(F1*) 87.78 등으로 SOTA를 갱신. 전문가 3인 human evaluation에서도 자동평가보다 높은 정확성을 확인(평가자 간 Kendall 0.91). 데이터스토어에 COVID-19 RCT 초록을 추가하면 재학습 없이 최신 답변을 생성(zero-shot datastore update).

## 한계점
- 청크가 근거의 부분만 담아 불완전·비사실 텍스트나 반복·모순을 유발할 수 있다.
- 청크가 단어/엔티티 경계를 가로질러 분할될 위험(생의학에서 특히 위험).
- 지식 베이스에 초록만 사용 → 데이터스토어 topic coverage가 성능 상한을 정한다(full-text 활용은 future work).
- 높은 메모리·FAISS 인덱스 디스크 소비; 백본 SCIFIVE가 적은 자원으로 학습되어 undertrained일 수 있음.

## 관련 정보
- ACL Anthology: https://aclanthology.org/2022.emnlp-main.390/ (EMNLP 2022, pp. 5770–5793)
- Code: https://github.com/disi-unibo-nlp
- 저자: Giacomo Frisoni, Miki Mizutani, Gianluca Moro, Lorenzo Valgimigli (University of Bologna)
