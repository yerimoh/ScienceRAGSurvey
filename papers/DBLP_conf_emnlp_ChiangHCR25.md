---
notion_id: 355f2dcd-4912-8174-b0ad-da33b24ce8e1
title: LLaMP - Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval
bib_key: DBLP:conf/emnlp/ChiangHCR25
year: 2025
domain: material, chem
type: benchmark
venue: EMNLP
paper_link: https://arxiv.org/abs/2401.17244
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# LLaMP: Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval

> arXiv | 2024 | Benchmark | material, chem

## 한 줄 요약
LLM 및 RAG 기반 에이전트 시스템이 수치형 재료 과학 데이터를 얼마나 정확하고 일관되게 추출·예측하는지 측정하기 위해 Materials Project 기반으로 구성한 자체 평가셋.

## 제작 배경
- 기존의 LLM 평가는 주로 텍스트 기반 답변에 치중되어 있어, 정밀도가 요구되는 고위험 과학 분야(예: Self-driving Labs)에서 실사용 가능 수준인지 확인하기 어려움.
- 모델의 환각 여부뿐만 아니라 답변을 산출할 때의 '일관성(Consistency)'을 정량화할 통계적 평가 기준이 필요함.

## 어떻게 만들었나 (Construction Methodology)
- **Step 1: 데이터 출처 선정**: 평가 기준 데이터(Ground Truth)로 제일원리 계산 기반의 대규모 개방형 데이터베이스인 Materials Project(MP)를 채택.
- **Step 2: 구축 파이프라인**: 3d 전이금속(체적 탄성률 평가), 일반/다원소 화합물(밴드갭 평가), 그리고 일반 생성 에너지 평가를 위한 특정 재료 리스트 구성.
- **Step 3: 서브셋 구축**: MP에 등록된 모든 단일·이원·삼원 화합물 모집단에서 무작위로 800개의 재료를 추출하여 자기 정렬(Magnetic ordering) 및 총 자화(Total magnetization) 평가 서브셋 구축.

## Input (입력)
- **출처**: Materials Project Database
- **문항 형식**: 자연어 질문
- **도메인**: 재료 물성(열역학적, 기계적 특성, 전자 구조) 및 자기적 특성
- **측정 대상**:

| 대상 특성 | 데이터 형태 |
|---|---|
| Bulk Moduli (K) | GPa 단위의 체적 탄성률 수치 |
| Formation Energy (ΔH_f) | eV/atom 단위 수치 |
| Electronic Bandgap (E_g) | eV 단위 (Common 및 Multi-element 구분) |
| Magnetic Ordering | 분류 태스크 (FM, AFM, FiM, NM) |

## Output (출력 / 정답 형식)
- **수치 회귀형 평가 지표**:
	- MAE (Mean Absolute Error)
	- SCoR (Self-consistency of Response): Precision, CoP, Confidence를 결합해 0~1 범위로 답변의 재현성·일관성 산출
- **분류형 평가 지표**: Accuracy, F1 Score, R²

## 예시 문항
- Q: "What are the bulk moduli of the following metals: Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn?"
- A: "Scandium (Sc): Voigt=45.715, Reuss=45.34, VRH=45.528 ... Zinc (Zn): Voigt=76.283, Reuss=95.46, VRH=85.872" (단위 GPa)

## 주요 평가 결과
- 도메인 특화 LLM 프롬프팅 방식(StructChem)이나 일반 바닐라 모델(Llama 3-8b, Gemini-Pro 등)은 생성 에너지나 다원소 밴드갭 예측에서 환각으로 인해 매우 큰 오차(높은 MAE)와 0에 가까운 SCoR 수치를 보임.
- LLaMP 프레임워크가 체적 탄성률 예측 시 바닐라 모델(GPT-4 기준 MAE 41.225) 대비 오차를 크게 줄임(MAE 14.574).

## 한계점
- 특정 모델의 Function-calling 역량에 따라 측정 성능이 직접적인 영향을 받음.
- Materials Project가 담고 있는 수치 자체가 이론적 한계(예: GGA 밴드갭 과소평가)를 가지고 있으므로, 실험적 Ground Truth와의 괴리가 있을 수 있음.

## 관련 정보
- 논문 링크: [https://arxiv.org/abs/2401.17244](https://arxiv.org/abs/2401.17244)
- 이 벤치마크를 사용한 논문:
	- LLaMP 원본 논문 (arXiv 2024)
