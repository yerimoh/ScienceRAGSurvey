---
notion_id: 355f2dcd-4912-81f0-8a5b-d3def3dd9529
title: Materials Dual-Source Knowledge Retrieval-Augmented Generation for Local Large Language Models in Photocatalysts
bib_key: DBLP:journals/jcisd/TakaharaYOKHTTKF25
year: 2025
domain: material, chem
type: Method
venue: J. Chem. Inf. Model.
paper_link: https://doi.org/10.1021/acs.jcim.5c01941
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Materials Dual-Source Knowledge Retrieval-Augmented Generation for Local Large Language Models in Photocatalysts

> J. Chem. Inf. Model. | 2025 | Method | material, chem

## 한 줄 요약
CSV 실험 데이터와 PDF 문헌을 이중 소스로 통합하여, 완전 오프라인 환경에서 로컬 LLM을 광촉매 재료 도메인에 특화시키는 RAG 프레임워크(MDSK-RAG).

## 연구 배경 및 동기
- **기존 방법의 한계점**: 클라우드 기반 LLM(예: GPT-4o)은 성능이 우수하나, 연구실 내 미공개 실험 데이터를 다루는 환경에서 데이터 기밀성 문제로 외부 API 활용이 불가. 기존 RAG는 주로 텍스트 문헌만 다루며, 연구실 자체 보유 CSV 실험 데이터를 통합하는 방법이 부재.
- **이 연구가 필요한 이유**: 실험실 환경에서 비공개 실험 레코드와 과학 문헌을 동시에 활용하면서도 완전한 오프라인 운용이 가능한 도메인 특화 RAG 시스템이 필요. 모델 재학습(fine-tuning) 없이 로컬 LLM의 전문성을 빠르게 끌어올릴 수 있는 실용적 방법론 요구.

## 시스템 아키텍처
```
[사용자 쿼리]
    |
    +---> [CSV Retriever] --> CSV 변환 텍스트 DB (740 records) --> 관련 k개 passage 추출 --> 로컬 LLM 요약
    |
    +---> [PDF Retriever] --> PDF 문헌 DB (20 papers)         --> 관련 k개 passage 추출 --> 로컬 LLM 요약
    |
    +---> [두 요약 병합 + 원본 쿼리] --> 로컬 LLM (gemma-2-9b-it) --> 최종 응답 생성
```

## 핵심 모듈 상세 설명
### 1. 이중 데이터베이스 구성
| 소스 | 내용 | 규모 | 공개 여부 |
|---|---|---|---|
| CSV 실험 레코드 | 자체 금속황화물 광촉매 실험 데이터 | 740건 | Private |
| PDF 과학 논문 | 동료심사 완료 과학 논문 | 20편 | Private |

### 2. CSV → Template-based Text 변환
- 구조화된 CSV 테이블 데이터를 자연어 템플릿 텍스트로 변환하여 벡터 검색 가능하게 전처리.
- 예: `{재료명}의 수소 발생률은 {값} μmol/h이며, 조건은 {조건}이다.` 형태로 변환.

### 3. Dual Retriever
- CSV 변환 텍스트용 Retriever와 PDF용 Retriever를 독립 구성.
- 코사인 유사도 기반 벡터 검색으로 각각 k개 관련 passage 반환.
- 모든 연산 완전 로컬 처리(no-Internet).

### 4. Post-retrieval: 요약 및 병합
- 각 retriever 결과를 로컬 LLM이 개별 요약.
- 두 요약을 병합(fusion)하여 원본 쿼리와 함께 최종 생성 LLM에 입력.

### 5. Generator (로컬 LLM)
| 모델 | 크기 | 하드웨어 |
|---|---|---|
| gemma-2-9b-it (primary, quantized) | ~9B | 노트북 GPU (16GB VRAM) |
| Qwen2.5-7B-Instruct | ~7B | 노트북 GPU |
| gemma-2-27b-it | ~27B | 전용 서버 (RTX 3090, 24GB VRAM) |

## 실험 및 평가
### 평가 태스크 및 데이터셋
- **Photocatalyst Expert QA**: 도메인 전문가가 정의한 14개 질문으로 구성된 자체 제작 벤치마크.
- 질문 유형: 실험 조건 관련 사실형, 추론·해석형 혼합.

### 주요 결과
| 모델 | 조건 | Cosine Similarity (중앙값) | Expert 5점 평가 (중앙값) |
|---|---|---|---|
| gemma-2-9b-it | Without MDSK-RAG | 0.63 | 2 |
| gemma-2-9b-it | With MDSK-RAG | 0.71 (+12.70%) | 3 (+50.00%) |
| GPT-4o | Without MDSK-RAG (cloud) | 0.66 | — |

- Wilcoxon signed-rank test: W=14.0, p=1.34×10⁻² (통계적으로 유의)
- MDSK-RAG 적용 gemma-2-9b-it이 GPT-4o(without RAG)를 코사인 유사도 기준으로 상회.

## 핵심 기여
- CSV(실험 레코드)와 PDF(문헌) 이중 소스를 통합하는 최초 수준의 오프라인 재료과학 RAG 프레임워크 제안.
- 모델 재학습 없이 로컬 소형 LLM(<10B)의 도메인 전문성을 강화.
- 기밀 실험 데이터를 외부 유출 없이 활용 가능한 실용적 솔루션 제시.
- 10B 미만 로컬 LLM + MDSK-RAG가 고성능 클라우드 모델(GPT-4o, without RAG)을 특정 도메인에서 능가함을 실증.

## 한계점
- 추론형 질문에서 불완전한 컨텍스트 검색 시 오류 추론 유발 (reasoning failure mode 존재).
- 금속황화물 광촉매 도메인에 특화되어 있어 타 재료계 적용 시 도메인별 조정 필요.
- 평가 벤치마크가 14개 질문으로 소규모 (통계적 파워 제한).
- 향후 과제: 하이브리드 심볼릭 접근법, 도메인 특화 지식 그래프 구축 등 제안.

## 관련 연구 및 관련 정보
- **논문 링크**: [https://doi.org/10.1021/acs.jcim.5c01941](https://doi.org/10.1021/acs.jcim.5c01941)
- **관련 방법론**: HoneyComb, G-RAG, TopoChat (재료과학 RAG 계열)
- **사용 벤치마크**: Photocatalyst Expert QA (자체 제작, 14문항)
