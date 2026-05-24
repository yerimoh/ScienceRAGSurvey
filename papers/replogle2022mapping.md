---
notion_id: 355f2dcd-4912-8156-9420-cc42270da4bf
title: Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq
bib_key: replogle2022mapping
year: 2022
domain: bio
type: benchmark
venue: Cell
paper_link: https://doi.org/10.1016/j.cell.2022.05.013
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq

> Cell (2022) + bioRxiv (2024) | benchmark | bio
## 📌 한 줄 요약
CRISPRi 기반 대규모 단일 세포 Perturb-seq 데이터셋. 4개 인간 세포주, 2,023개 유전자 억제 조건, ~0.6M 세포로 구성된 in silico perturbation 예측 벤치마크 데이터셋.
## 🎯 제작 배경
### 기존 벤치마크의 한계
- 이전 perturbation 예측 데이터셋들(Norman, Adamson 등)은 수화된 센 단일 세포주와 적은 perturbation 수로 제한됨
- 세포 유형 간 일반화(cross-cell-type generalization) 평가가 불가능했던 데이터셋이 없었음
- 조합 perturbation만을 다루는 데이터셋(GEARS)vs 다중 세포주 평가 불가

### 왜 이 데이터셋이 필요했는지
- Genome-scale CRISPRi로 **수체의 필수 유전자(essential genes)** 대부분을 커버하는 대규모 시도 가능
- **4개 이상의 세포주** 포함으로 cell-type-aware 모델 평가 가능
- 통일된 전처리 스킬(HVG 2,000개, CRISPRi)로 일관된 비교 환경 제공
## 🔨 어떻게 만들었나 (Construction Methodology)
**Step 1: 데이터 출처 선정**
- Replogle et al. (2022, Cell): Genome-scale Perturb-seq 실험. Weissman 연구실(UCSF)에서 CRISPRi를 사용하여 K562 및 RPE1 세포주에서 ~10,000개 필수 유전자 knockdown
- Nadig et al. (2024, bioRxiv): 추가 세포주(Jurkat, HepG2) 포함으로 확장

**Step 2: 구축 파이프라인**
- CRISPRi 바이러스 라이브러리 설계 → 세포 케집 (pooled CRISPR screen)
- 10x Genomics Chromium 플랫폼으로 단일 세포 RNA 시퀀싱
- 코드(바코드) 기반 유전자 억제 확인, 세포 할당
- 제어 세포(non-targeting)vs 억제 세포 환경 구분

**Step 3: 품질 검증**
- 세포 품질 QC: 미토콘드리얼 유전자 마커, 검주율(doublet) 필터링
- 바코드 QC: 액세스 1개만 혹은 활성 2개 이상 필터링
- 억제 효율 검증: DE gene 수 및 억제 강도 확인

**Step 4: 데이터셋 구성 및 공개**
- 구링 방식: STATE (Adduri et al. 2025) 전처리 방식 준수 — 학습/테스트 분할
- 테스트용 perturbation: 1,635개
- CellxGene 등을 통해 공개 배포 (h5ad 포맷)
## 📥 Input (입력)
| 항목 | 내용 |
| 출처 | Replogle et al. 2022 (Cell) + Nadig et al. 2024 (bioRxiv) |
| 데이터 유형 | single-cell RNA-seq (Perturb-seq) |
| 알고리즘 | CRISPRi (CRISPR interference, 유전자 발현 억제) |
| 총 세포 수 | ~0.6M |
| 커버 유전자 | ~2,023개 (아미노산 tRNA 합성 등 필수 유전자 중심) |
| 세포주 | K562 (CML), RPE1 (망막 상피), Jurkat (T세포), HepG2 (간암) |
| 특징 차원 | 2,000 HVGs (Highly Variable Genes) |
| 형식 | h5ad (AnnData) |

## 📤 Output (출력 / 정답 형식)
- **출력 형태**: perturbation 후 세포의 전사체 발현 프로파일 (실수 수치 미덕 [float])
- **평가 지표**: W1, W2 (Wasserstein distance), DE-Spearman, Pearson Δ, MSE, MAE, PDS
- **특이사항**: 질병(distribution-level) 정확도와 개별 유전자 수준 정확도를 모두 요구; 세포 유형별 일반화 능력 평가 가능
## 📊 주요 평가 결과 (PT-RAG 논문 기준)
| 모델 | W2 (↓) | 비고 |
| PT-RAG (제안) | STATE 대비 개선 | 최우수 |
| STATE | 646.1 | 이전 SOTA |
| Vanilla RAG | 1189.5 | 검색이 오히려 해로운 경우 |
| GEARS | — | GNN 기반 baseline |

## ⚠️ 한계점
- 필수 유전자(essential genes)에 집중됨 — 으시적 으로 높은 폈두리 업전사 내 유전자에만 편향됨
- CRISPRi 억제만 평가됨 (증폭 기반 시도 미포함)
- 조합 perturbation 없음
## 🔗 관련 정보
- **원 논문 (Replogle 2022)**: [https://doi.org/10.1016/j.cell.2022.05.013](https://doi.org/10.1016/j.cell.2022.05.013)
- **Nadig 2024**: [https://doi.org/10.1101/2024.11.22.624843](https://doi.org/10.1101/2024.11.22.624843)
- **이 데이터셋을 사용한 논문**:
	- PT-RAG (Di Francesco et al., Gen2 @ ICLR 2026)
	- STATE (Adduri et al. 2025)
	- PerturbDiff (2026)
