---
notion_id: 355f2dcd-4912-812a-bbf9-cf63ebea591e
title: "Fact or Fiction: Verifying Scientific Claims"
bib_key: DBLP:conf/emnlp/WaddenLLWZCH20
year: 2020
domain: bio, medical
type: Method
venue: EMNLP
paper_link: https://aclanthology.org/2020.emnlp-main.609/
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Fact or Fiction: Verifying Scientific Claims

> EMNLP | 2020 | Method | bio · medical
## 📌 한 줄 요약
과학적 문헌에서 주어진 클레임의 사실 여부(SUPPORTS/REFUTES)를 판별하고 근거 문장을 찾는 3단계 파이프라인 시스템(VERISCI) 개발 및 전문가 주석 데이터셋(SCIFACT) 구축.
## 🎯 연구 배경 및 동기
- **기존 방법의 한계**: FEVER 등 기존 팩트체킹 데이터셋은 위키피디아 기반이거나 인위적으로 조작된 클레임을 사용하여 과학 분야 특유의 배경지식과 복잡한 언어 구조 미반영
- **이 연구가 필요한 이유**: 코로나19같은 보건 위기 상황에서 연구 문헌을 바탕으로 과학적 주장의 진위를 검증하고 근거를 신속하게 찾는 자동화 시스템이 필수적임
## 🏗️ 시스템 아키텍처
```javascript
[입력 Claim]
      │
      ▼
[ABSTRACTRETRIEVAL]
TF-IDF (unigram + bigram) 기반
상위 k=3개 관련 초록 검색
      │
      ▼
[RATIONALSELECTION]
각 초록 내 문장 단위 검사
클레임 지지/반박 근거 문장(선택)
      │
      ▼
[LABELPREDICTION]
RoBERTa-large 기반 분류기
SUPPORTS / REFUTES / NOINFO
```
## 🔑 핵심 모듈 상세 설명
### 1. ABSTRACTRETRIEVAL
- TF-IDF(unigram + bigram)를 사용하여 클레임과 가장 유사한 상위 k=3개 관련 문헌 초록을 검색
- 파인튜닝 없는 비파라미터 검색기
### 2. RATIONALSELECTION
- RoBERTa-large 모델로 각 문장이 클레임의 근거가 될 수 있는지 이진 분류
- 근거 문장(Rationale)을 필터링하여 다음 단계로 전달
### 3. LABELPREDICTION
- 추출된 근거 문장들 + 클레임을 RoBERTa-large 분류기에 입력
- **FEVER 데이터셋**으로 사전학습 후 SCIFACT로 파인튜닝 시 성능 크게 향상
- Oracle(정답 초록 제공) 환경에서 Abstract Label+Rationale F1 약 72.6%
## 🧪 실험 및 평가
**평가 환경 및 결과 (SCIFACT)**
<table header-row="true">
<tr>
<td>조건</td>
<td>Abstract Label-Only F1</td>
<td>Abstract Label+Rationale F1</td>
</tr>
<tr>
<td>Oracle Abstract</td>
<td>~89.7%</td>
<td>~72.6%</td>
</tr>
<tr>
<td>Oracle Rationale</td>
<td>—</td>
<td>~72.0%</td>
</tr>
<tr>
<td>Open (TF-IDF 검색)</td>
<td>~64.1%</td>
<td>~46.4%</td>
</tr>
</table>
**CORD-19 케이스 스터디**
- 코로나19 관련 클레임에 대해 의대생 평가 포함
- Lopinavir/ritonavir 등 실제 임상 코맨트에서 가능한 근거 잘 추출
## 💡 핵심 기여
1. 과학적 클레임 검증(Scientific Claim Verification)이라는 새로운 태스크 공식화
2. 논문 인용구(Citance) 기반의 자연스러운 1.4K개 전문가 주석 데이터셋(SCIFACT) 구축 및 공개
3. 도메인 특화 데이터 및 사전학습을 활용한 강력한 베이스라인(VERISCI) 구축
## ⚠️ 한계점
- 인과관계 추론, 통계적 수치(p-value, 신뢰구간) 해석, 상호참조(Coreference) 해결, 감역 특화 배경지식 요구되는 부분에서 여전히 오류 발생
## 🔗 관련 연구 및 관련 정보
- **논문**: [https://aclanthology.org/2020.emnlp-main.609/](https://aclanthology.org/2020.emnlp-main.609/)
- **GitHub (SCIFACT)**: [https://github.com/allenai/scifact](https://github.com/allenai/scifact)
- **참조**: CORD-19 (Wang et al., 2020), FEVER (Thorne et al., 2018)
