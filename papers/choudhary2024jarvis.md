---
title: "JARVIS-Leaderboard: A Large-Scale Benchmark of Materials Design Methods"
bib_key: "choudhary2024jarvis"
year: 2024
domain: material, chem, physics
type: benchmark
venue: npj Computational Materials
paper_link: https://doi.org/10.1038/s41524-024-01259-w
---
# JARVIS-Leaderboard: ~1,500 Tasks × 11 Categories Multi-modal Materials Benchmark

> npj Computational Materials 10:93 | 2024 | Benchmark (multi-verifier materials platform) | material · chem · physics
> Kamal Choudhary, Daniel Wines, Kevin F. Garrity, et al. (Maureen Williams, Francesca Tavazza, Kangming Li, Jason Hattrick-Simpers, Vishu Gupta, Aldo H. Romero, Jaron T. Krogel, Kayahan Saritas, Addis Fuhr, Panchapakesan Ganesh, Paul R. C. Kent, Keqiang Yan, Yuchao Lin, Shuiwang Ji, Ben Blaiszik, Patrick Reiser, Pascal Friederich, Ankit Agrawal, ...) — NIST / Argonne / ORNL / Toronto / Texas A&M / KIT
> arXiv: [2306.11688](https://arxiv.org/abs/2306.11688) · DOI: [10.1038/s41524-024-01259-w](https://doi.org/10.1038/s41524-024-01259-w)

## 한 줄 요약
NIST에서 운영하는 **AI4Materials 통합 benchmark platform**. **~1,500 tasks × 11 categories** 규모로 **DFT, AIMD, classical force field, 실험적 측정**을 verifier로 포함하는 multi-modality 평가. 152 methods, **8M+ data points** 비교, 지속 확장형 leaderboard.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 11 categories of materials design tasks
  ┌──────────────────────────────────────────────┐
  │ 1. Bulk DFT properties (band gap, formation E)│
  │ 2. AIMD / molecular dynamics simulations     │
  │ 3. Force field development & evaluation      │
  │ 4. Defect properties (vacancies, dopants)    │
  │ 5. Phonon properties                          │
  │ 6. Electronic structure (DFT/GW/DMC)         │
  │ 7. Experimental measurements (XRD, ARPES, etc.)│
  │ 8. Quantum computing for materials           │
  │ 9. Symmetry & space group classification     │
  │ 10. Text / NER / image classification         │
  │ 11. Structure-property prediction at scale   │
  └──────────────────────────────────────────────┘

Step 2 — Multi-verifier framework
  Each task can be verified by:
    · DFT calculation (PBE/HSE/SCAN 등 다양한 functional)
    · AIMD molecular dynamics
    · Empirical force field
    · Experimental measurement (XRD pattern, photoemission, etc.)

Step 3 — Scale
  ┌────────────────┬──────────────────────────┐
  │ Tasks          │ ~1,500                    │
  │ Categories     │ 11                        │
  │ Methods compared│ 152                       │
  │ Data points    │ 8,000,000+                │
  │ Submissions    │ 지속 확장                  │
  └────────────────┴──────────────────────────┘

Step 4 — User contributions
  └─ Custom task 설정 가능 (사용자 benchmark 추가)
  └─ Dataset / methods / metrics 제출 인터페이스
  └─ Globus 호스팅 (대용량 데이터)
```

---

## 실제 데이터 형식 예시 (논문 §I + Figure 1 + §Abstract)

### 유형 A — Benchmark task naming convention

> JARVIS-Leaderboard에서 task는 `Category-Subcategory-Target-Dataset-Split-Metric` 형식:
>
> ```
> AI-SinglePropertyPrediction-formation_energy_peratom-dft_3d-test-mae
>    │                       │                          │       │    │
>    Category                Target property            Dataset Split Metric
> ```
>
> 예시 task 들:
> - `AI-SinglePropertyPrediction-bandgap_opt_HSE-dft_3d-test-mae`
> - `ES-SinglePropertyPrediction-bandgap_HSE-silicon-test-mae`
> - `FF-SinglePropertyPrediction-cohesive_energy-bulk_silicon-test-mae`
> - `QC-SinglePropertyPrediction-ground_state_energy-H2-test-mae`
> - `EXP-SinglePropertyPrediction-bandgap-silicon-test-mae`

### 유형 B — 5 카테고리 coverage

> ```
> ┌──────────────────────────────────────────────┐
> │ AI  (Artificial Intelligence)                │
> │  · Input: atomic structure / image / spectra │
> │           / text                              │
> │  · 예: formation energy 예측 ALIGNN/MEGNet 등 │
> │                                              │
> │ ES  (Electronic Structure)                   │
> │  · DFT (PBE/SCAN/HSE) / GW / DMC             │
> │  · 다양한 software, pseudopotential 비교     │
> │                                              │
> │ FF  (Force-fields)                            │
> │  · 고전 FF · ML interatomic potential        │
> │  · 결정 안정성, 표면, defect                 │
> │                                              │
> │ QC  (Quantum Computation)                    │
> │  · Hamiltonian simulation, VQE 등 회로        │
> │                                              │
> │ EXP (Experimental)                            │
> │  · XRD, ARPES, XPS, magnetometry 등           │
> │  · inter-laboratory benchmark                 │
> └──────────────────────────────────────────────┘
> ```

### 유형 C — Submission 구조 (contribution 단위)

> 각 leaderboard 기여는 다음 4개 파일 묶음:
>
> ```
> contribution_folder/
> ├── *.csv.zip       — 모델 예측값 (or 실험 측정값)
> ├── run.sh          — 재현 shell script
> ├── metadata.json   — team / DOI / software ver / hardware / wall-time
> └── Dockerfile      — environment specification (optional)
> ```
>
> 자동 비교 reference data는 `benchmarks/<category>/<target>.json.zip` 에 사전 등록.

### 유형 D — Scale 통계 (논문 Abstract)

> ```
> ┌─────────────────────────┬────────────┐
> │ Total benchmarks         │   274      │
> │ Total contributions      │ 1,281      │
> │ Methods compared         │   152      │
> │ Total data points        │ 8,000,000+ │
> │ Categories               │     5 (+조합)│
> └─────────────────────────┴────────────┘
> ```
>
> 한 task (예: formation energy of silicon)에 17+ ES method 결과가 모두 등록되어 inter-method 비교 가능.

---

## 평가 framework

| 차원 | 옵션 |
|---|---|
| Output type | property regression / classification / image / text / quantum |
| Verifier | DFT (PBE/HSE/SCAN) / AIMD / FF / experiment / human |
| Reference data | NIST JARVIS database + 외부 기여 |
| Submission | dataset + method + metric tuple |
| Public score | 자동 leaderboard 갱신 |

---

## 주요 활용

| 항목 | 내용 |
|---|---|
| Materials foundation model 평가 | 단일 task 외 다중 verifier 평가 |
| 다중 modality | DFT + experiment + ML | 
| 후속 작업 | Matbench Discovery (subset), MLIP Arena (subset), 등 |

---

## 한계점
- **Coverage 편향**: bulk crystal 위주, surface/molecular 부족
- **DFT functional 비교 어려움**: 다른 functional 결과 직접 비교 시 caveat 필요
- **사용자 기여 품질 관리**: 다중 contributor 환경에서 데이터 품질 균일성 보장 어려움
- **실험 데이터 sparsity**: 실험 verifier가 가능한 task 한정
- **Continual expansion**: snapshot 비교 시 시점 통일 필요
- **NIST 인프라 의존**: NIST 호스팅 종료 시 데이터 접근 위험

---

## 관련 정보
- **논문 (npj CompMat)**: [10.1038/s41524-024-01259-w](https://doi.org/10.1038/s41524-024-01259-w)
- **arXiv**: [2306.11688](https://arxiv.org/abs/2306.11688)
- **공식 사이트**: [pages.nist.gov/jarvis_leaderboard](https://pages.nist.gov/jarvis_leaderboard/)
- **NIST JARVIS**: [jarvis.nist.gov](https://jarvis.nist.gov/)
- **GitHub**: [usnistgov/jarvis_leaderboard](https://github.com/usnistgov/jarvis_leaderboard)
- **이 benchmark를 사용한 후속 작업**: 다양한 materials foundation model 평가, MLIP cross-checks
