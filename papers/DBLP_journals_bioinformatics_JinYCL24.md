---
title: "GeneGPT: augmenting large language models with domain tools for improved access to biomedical information"
bib_key: "DBLP:journals/bioinformatics/JinYCL24"
year: 2024
domain: bio, medical
type: Method
venue: Bioinformatics
paper_link: https://arxiv.org/abs/2304.09667
---
# GeneGPT: LLMs Calling NCBI Web APIs for Genomics QA
> Bioinformatics 2024 | Method | bio · medical

## 한 줄 요약
GeneGPT는 Codex(code-davinci-002)에게 in-context learning으로 NCBI Web API(E-utils + BLAST) 사용법을 가르치고, 디코딩 중 API 호출을 감지·실행해 그 raw 결과를 생성 텍스트에 다시 끼워넣는(augmented decoding) 방식으로 유전체 QA를 수행한다. GeneTuring 9개 태스크 평균 0.83으로 직전 최고 New Bing(0.44)을 크게 능가한다.

## 시스템 구조 (GeneGPT Architecture)
- **NCBI Web APIs:** ① E-utils(`esearch`/`efetch`/`esummary`) — `gene`/`snp`/`omim` DB에서 식별자·요약 조회. ② BLAST URL API(`CMD=Put`→`Get`, `blastn`, `nt` DB) — 서열 정렬.
- **In-context prompt(4부):** instruction + documentation(API 문법) + demonstration(NCBI API로 푸는 예시 4개; URL/결과를 `[ ]`로 감싸고 `->`를 호출 indicator로 사용) + test question. (전부 사용=full, Dm.1+Dm.4만=slim)
- **Augmented decoding:** 생성 중 `->` 토큰을 만나면 마지막 URL을 추출해 NCBI API를 호출하고 raw 결과를 텍스트에 삽입한 뒤 생성을 재개. `\n\n`이면 종료하고 "Answer:" 이후를 답으로 추출.

## 동작 파이프라인 (inference)
1. prompt(instruction+doc+demo+질문) 구성, Codex(temperature 0)로 생성.
2. `->` 감지 → URL 추출 → E-utils/BLAST 호출 → 결과 삽입 → 재개.
3. 한 질문에 여러 API를 연쇄(esearch→efetch; BLAST Put→Get). multi-hop(GeneHop)은 CoT로 서브질문 분해.
4. `\n\n` → 종료 → 답 추출.

## 주요 결과
GeneTuring(12 태스크 중 NCBI 관련 9개, 각 50문항):

| 모델 | Overall avg |
|---|---|
| GPT-3 (davinci-003) | 0.16 |
| ChatGPT | 0.12 |
| New Bing | 0.44 |
| **GeneGPT-slim** | **0.83** |

- 직전 SOTA New Bing(0.44) 대비 큰 폭 향상. Sequence alignment(BLAST)에서 다른 모든 모델은 ~0.00, GeneGPT 0.66.
- GeneHop(multi-hop, 신규) 평균: GeneGPT 0.50 vs New Bing 0.24.
- Ablation: API demonstration이 documentation보다 in-context 학습에 유용, cross-task 일반화 강함.

## 한계점
- 자동 exact-match 평가(비교군은 원 벤치마크 수동 평가)라 기준이 동일하지 않음.
- 일부 질문은 NCBI DB만으로 답 불가(E4 오류), 인자 오류(E2)·결과 추출 실패(E3) 존재.
- Codex(8k context·코드 이해) 의존, NCBI 서버 접근 필요.

## 관련 정보
- arXiv: 2304.09667 · Bioinformatics 2024 (Jin, Yang, Chen, Lu; NCBI/NLM)
- 도구: NCBI E-utils(gene/snp/omim) + BLAST(blastn, nt)
