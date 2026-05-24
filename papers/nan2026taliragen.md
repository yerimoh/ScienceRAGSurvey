---
notion_id: 355f2dcd-4912-8113-a854-f25bfbf12882
title: TaLiRAGen: target-aware ligand generation via RAG LLMs
bib_key: nan2026taliragen
year: 2026
domain: chem, bio, medical
type: Method
venue: Molecular Diversity
paper_link: https://doi.org/10.1007/s11030-026-11483-9
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# TaLiRAGen: target-aware ligand generation via RAG LLMs

> Molecular Diversity (Springer Nature) | 2026 | Method | chem · bio · medical
## 📌 한 줄 요약
RAG와 LLM을 결합하여, 타겟 특화 학습 없이 단백질 타겟에 맞는 리간드를 생성하는 no-training 프레임워크.

사전지식: 리간드 - 리간드(ligand)는 특정 단백질(주로 수용체나 효소)에 결합하는 작은 분자입니다. 약물 개발에서 핵심 개념인데, 어떤 질병과 관련된 단백질이 있으면, 그 단백질에 딱 맞게 결합해서 기능을 억제하거나 활성화하는 분자를 설계하는 것입니다. TaLiRAGen 논문에서는 바로 이 리간드를 AI로 설계하는 게 목표예요. 특정 타겟 단백질을 주면, 거기에 잘 붙을 것 같은 분자 구조(SMILES 형식)를 LLM+RAG로 생성하는 거죠. 결합 잘 되는지는 AutoDock Vina라는 도킹 소프트웨어로 시뮬레이션해서 점수를 매김.

## 🎯 연구 배경 및 동기
**기존 방법의 한계점:**
- VAE, 확산 모델(diffusion model) 등 생성 모델은 타겟 특화 학습 데이터에 심하게 의존하여, 데이터가 부족한 새로운 타겟에 적용하기 어려움.
- 기존 방법들은 LLM에 이미 내재된 방대한 생화학 지식을 충분히 활용하지 못함.

**이 연구가 필요한 이유:**
- 구조 기반 신약 설계(Structure-Based Drug Design, SBDD)에서 특정 단백질 타겟에 높은 결합 친화도를 가지는 리간드를 생성하는 것은 핵심 과제임.
- 학습 없이도 LLM의 일반 화학 지식과 외부 데이터베이스 검색을 결합하면, 다양한 타겟에 유연하게 적용 가능한 리간드 생성이 가능함.
## 🏗️ 시스템 아키텍처
```javascript
[Input: 단백질 타겟 구조 / 서열]
        ↓
[Retriever] protein-ligand context를 diverse repositories에서 검색
        ↓
[CoT-augmented Multi-turn Prompting] — 검색된 context를 LLM에 통합
        ↓
[LLM Generator] — SMILES 형식 리간드 후보 생성
        ↓
[Docking Feedback (AutoDock Vina)] — 결합 친화도 계산, 낮은 후보 필터링
        ↓
[Evidence-Theoretic Normalization 통합 평가] — QED + SA + Vina score 통합
        ↓
[Output: 구조적 제약 조건을 만족하는 최적 리간드 후보]
```
[image]
## 🔑 핵심 모듈 상세 설명
**① RAG 기반 Retrieval**
- 단백질-리간드 맥락(context)을 다양한 저장소(diverse repositories)에서 검색.
- 검색된 context는 유사한 단백질-리간드 쌍 정보를 포함하여 LLM의 생성 방향을 안내.

**② CoT-augmented Multi-turn Prompting**
- Chain-of-Thought 추론을 멀티턴 대화 형식에 결합하여, LLM이 생화학적 맥락을 단계적으로 처리.
- LogP, ring count 등 구조적 제약 조건을 프롬프트에 명시하여 맞춤형 리간드 생성 가능.

**③ Docking Feedback 기반 정제**
- AutoDock Vina를 이용해 생성된 SMILES 리간드를 단백질 타겟에 도킹.
- 도킹 점수(Vina score)를 피드백으로 활용하여 분자를 반복적으로 정제(refinement).

**④ Evidence-Theoretic Normalization 통합 평가 지표**
- 결합 친화도(binding affinity)와 약물 유사성(drug-like properties)을 증거 이론적 정규화(evidence-theoretic normalization)로 통합.
- QED(약물 유사성 정량 추정), SA(합성 접근성), Vina docking score를 하나의 지표로 통합 평가.
## 🧪 실험 및 평가
**평가 태스크 및 데이터셋:**
- **CrossDocked2020** test set 사용. 969 target IDs에서 적절성·신뢰성 기준 필터링 후 **908 targets** 최종 사용.
- 타겟당 **5개 리간드** 생성 후 평가.
- AutoDock Vina를 통한 도킹 점수 기반 평가.

**주요 평가 지표:**
| 지표 | 설명 |
| Vina docking score | 결합 친화도 (낮을수록 좋음, kcal/mol) |
| QED | 약물 유사성 정량 추정 (0~1, 높을수록 좋음) |
| SA | 합성 접근성 (0~1, 높을수록 좋음) |
| 통합 지표 | Evidence-theoretic normalization 적용, 위 세 지표 통합 |
| LogP, ring count 등 | 구조적 제약 조건 충족 여부 |

**비교 대상:**
- 기존 VAE 기반, 확산 모델 기반 SBDD 방법 대비 binding affinity 및 drug-likeness 비교 (구체적 수치는 전문 미확인).
## 💡 핵심 기여
- **No-training 프레임워크**: 타겟 특화 학습 없이 LLM 내장 화학 지식 + RAG로 리간드 생성 → 데이터 부족 타겟에도 적용 가능.
- **Evidence-theoretic normalization 통합 지표**: 결합 친화도 + 약물 유사성을 단일 지표로 통합하여 생성 리간드 평가 일관성 향상.
- **프롬프트 기반 구조 맞춤화**: LogP, ring count 등 구조 제약 조건을 프롬프트로 유연하게 반영 가능.
## ⚠️ 한계점
- 논문 전문 미공개로 사용된 specific DB명, LLM 모델명 확인 불가.
- SMILES 유효성(validity) 및 합성 가능성(SA) 검증이 계산적 수준에 머물러, 실험적 검증 부재.
- 도킹 기반 결합 친화도 평가는 실제 wet-lab 결합 친화도와 차이가 있을 수 있음.
- 생성된 리간드의 다양성(diversity) 및 신규성(novelty) 지표 상세 보고 여부 불명.
## 🔗 관련 연구 및 관련 정보
- **논문 링크**: [https://doi.org/10.1007/s11030-026-11483-9](https://doi.org/10.1007/s11030-026-11483-9)
- **코드/데이터**: GitHub ([https://github.com/yxjacksonyyds/T](https://github.com/yxjacksonyyds/T)), Google Drive 보충자료
- **PubMed**: [https://pubmed.ncbi.nlm.nih.gov/41723766/](https://pubmed.ncbi.nlm.nih.gov/41723766/)
- **키워드**: Structure-Based Drug Design (SBDD), Retrieval-Augmented Generation, Chain-of-Thought, AutoDock Vina, evidence-theoretic normalization, no-training ligand generation
