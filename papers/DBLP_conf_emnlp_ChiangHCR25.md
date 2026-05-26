---
title: LLaMP - Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval
bib_key: DBLP:conf/emnlp/ChiangHCR25
year: 2025
domain: material
type: Method
venue: EMNLP 2025
paper_link: https://arxiv.org/abs/2401.17244
---
# LLaMP: Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval

> EMNLP 2025 | Method + Benchmark | material
> Chiang, Hsieh, Chaudhuri, Rohrbach — UC Berkeley / Meta FAIR
> DBLP: `conf/emnlp/ChiangHCR25`

## 한 줄 요약
Materials Project API를 ReAct 에이전트 툴로 래핑하여 LLM이 DFT 계산 기반 물성 데이터를 직접 조회·검증하도록 하고, 수치형 재료 물성(체적 탄성률·밴드갭·생성 에너지·자기 순서)에 대한 정확도와 자기 일관성을 **SCoR(Self-Consistency of Response)** 지표로 측정하는 RAG 에이전트 시스템 및 평가 프로토콜.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 지식 소스 선정
  Materials Project (MP): 제일원리 DFT 계산 기반 대규모 재료 DB
  API를 통해 실시간 조회 가능

Step 2 — 평가 태스크 및 서브셋 구성
  태스크 A: Bulk Moduli (체적 탄성률, GPa)
    대상: 3d 전이금속 (Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn)
    Voigt / Reuss / VRH 세 가지 값 각각 평가

  태스크 B: Electronic Bandgap (eV)
    서브셋 1 (Common): 자주 참조되는 일반 화합물
    서브셋 2 (Multi-element): 3원 이상 복잡 화합물

  태스크 C: Formation Energy (ΔH_f, eV/atom)
    MP 등록 모든 단일·이원·삼원 화합물에서 무작위 800개 추출

  태스크 D: Magnetic Ordering (분류)
    FM / AFM / FiM / NM 4개 클래스
    무작위 800개 화합물 서브셋

Step 3 — ReAct 에이전트 툴 설계 (LLaMP 시스템)
  Materials Project → API 래퍼 툴(python-materials-project)
  ReAct 루프: Thought → Action(API 호출) → Observation → 반복
  최종 수치 답변 생성

Step 4 — SCoR 지표 정의
  동일 쿼리를 N회 반복 → 답변 분포 분석
  ┌─ Precision (CoP): 정답 수렴 비율
  ├─ Confidence: 분포 집중도
  └─ SCoR ∈ [0,1]: 세 요소 결합 → 재현성·일관성 종합 점수
  → MAE + SCoR로 정확도와 일관성을 동시 평가

Step 5 — 베이스라인 비교
  바닐라 LLM (GPT-4, Llama 3-8b, Gemini-Pro 등)
  도메인 특화 프롬프팅 (StructChem)
  LLaMP (ReAct + MP API)
```

---

## 실제 평가 문항 예시

### 태스크 A — Bulk Moduli
> **Q.** What are the bulk moduli of the following 3d transition metals: Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn?
>
> **LLaMP 답변 (API 조회):**
> Scandium (Sc): Voigt=45.715, Reuss=45.34, VRH=45.528 GPa
> Zinc (Zn): Voigt=76.283, Reuss=95.46, VRH=85.872 GPa ...

### 태스크 D — Magnetic Ordering (분류)
> **Q.** What is the magnetic ordering of BaTiO₃?
>
> (A) Ferromagnetic  (B) Antiferromagnetic  (C) Ferrimagnetic  **(D) Non-magnetic** ← 정답

---

## 주요 평가 결과

**체적 탄성률 (Bulk Moduli) — MAE 비교**
| 모델 | MAE ↓ | SCoR ↑ |
|---|---|---|
| GPT-4 (바닐라) | 41.225 | ~0.2 |
| StructChem | 38.1 | ~0.3 |
| Llama 3-8b | 환각 발생 | ~0 |
| **LLaMP (GPT-4 + MP API)** | **14.574** | **~0.8** |

**밴드갭 (Bandgap) — Multi-element 서브셋**
- 바닐라 GPT-4: MAE 매우 크고 SCoR ≈ 0 (환각)
- LLaMP: MAE 대폭 감소, SCoR 유의미하게 향상

**자기 순서 분류**
- 바닐라 모델: F1 낮음 (도메인 지식 부족)
- LLaMP: 정확도 및 F1 향상 (API 조회로 파라메트릭 오류 보완)

---

## 한계점
- Materials Project 값이 GGA DFT 계산 기반 → 실험값과 체계적 오차 존재 (밴드갭 과소평가 등)
- 모델의 function-calling 역량에 따라 측정 성능이 직접 영향받음
- ReAct 루프의 API 응답 파싱 실패 시 환각으로 퇴화 가능
- 커버리지: MP에 등록된 물질에 한정 (실험 합성 데이터 미포함)

---

## 관련 정보
- **논문**: [arXiv:2401.17244](https://arxiv.org/abs/2401.17244)
- **EMNLP 2025 Anthology**: [ACL Anthology](https://aclanthology.org/2025.emnlp-main)
- **Materials Project**: [materialsproject.org](https://materialsproject.org)
- **이 시스템을 사용한 논문**: HoneyComb (EMNLP Findings 2024)의 비교 대상으로 참조
