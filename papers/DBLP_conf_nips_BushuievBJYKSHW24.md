---
notion_id: 355f2dcd-4912-81e1-a354-c9c3bae54271
title: MassSpecGym - A benchmark for the discovery and identification of molecules
bib_key: DBLP:conf/nips/BushuievBJYKSHW24
year: 2024
domain: chem
type: benchmark
venue: NeurIPS
paper_link: https://proceedings.neurips.cc/paper_files/paper/2024/hash/c6c31413d5c53b7d1c343c1498734b0f-Abstract-Datasets_and_Benchmarks_Track.html
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# MassSpecGym: A benchmark for the discovery and identification of molecules

> NeurIPS | 2024 | Benchmark | chem

## 한 줄 요약
MS/MS 탠덤 질량 분석 데이터로부터 분자를 발견·식별하는 최초의 포괄적 벤치마크. 231k 스펙트럼·29k 분자를 포함하며, 세 가지 챌린지(de novo 생성, 분자 검색, 스펙트럼 시뮬레이션)와 일반화 요구 분할(MCES-based split)을 제공.

## 제작 배경
### 기존 벤치마크의 한계
- **표준 데이터셋 부재**: 기존 연구들이 각기 다른 이질적·비표준화 데이터셋 사용 → 결과 비교 불가
- **데이터 누출 문제**: 기존 Random split은 Tanimoto 유사도 > 0.85인 거의 동일한 분자를 train/test에 동시 포함 → 모델 성능 과대 평가
- **평가 프로토콜 불일치**: 연구마다 다른 메트릭·분할·캔디데이트 세트 사용
- **접근성 문제**: 전처리에 MS 전문 지식 필요 → ML 커뮤니티 진입 장벽 높음
- **상업용 데이터 의존**: NIST처럼 라이센스 필요한 데이터셋만 존재, 공개 재현 불가

### 왜 이 벤치마크가 필요했는가
- 생물·환경 샘플의 분자 발견·식별은 바이오메디컬·화학 과학의 핵심이나, 탠덤 질량 스펙트럼을 분자 구조로 디코딩하는 것은 전문가도 어려운 난제
- 수집된 MS/MS 스펙트럼의 대다수가 미해석 상태로 방치 → 화학 과정 이해 제한
- ML 방법 개발을 위한 표준 데이터셋·평가 기준 부재가 지속적인 병목

## 어떻게 만들었나 (Construction Methodology)
**Step 1: 데이터 출처 선정**
세 개의 대형 공개 스펙트럼 라이브러리를 통합:
- **MoNA (MassBank of North America)**: 크라우드소싱 MS/MS 라이브러리
- **MassBank**: 유럽 중심 공개 스펙트럼 라이브러리
- **GNPS (Global Natural Products Social Molecular Networking)**: 자연물 중심 공개 DB
- **In-house 측정 스펙트럼**: 자체 측정 신규 스펙트럼 (10,000 분자 규모)

선정 이유: 가장 크고 다양한 공개 데이터 통합 + 자체 측정으로 커버리지 확장, 상업용 의존 없음.

**Step 2: 구축 파이프라인**
```
원시 스펙트럼 수집 (MoNA + MassBank + GNPS + in-house)
    ↓
[메타데이터 정규화]
  - 필드명 통일, 잘못된 필드 수정
  - 누락 SMILES/InChI/InChIKey 보완
  - 누락 parent mass → SMILES 질량으로 도출
  - 누락 adduct → precursor m/z와 parent mass로 도출
    ↓
[품질 필터링]
  - adduct + precursor m/z로 계산한 parent mass ≠ SMILES mass 제거
  - 모노아이소토픽 질량 불일치 제거
  - 하전된 분자 어노테이션 제거
  - Brungs et al. MS/MS 라이브러리 병합 스펙트럼 제거
    ↓
[SMILES 표준화]
  - 표준화 실패 화합물 제거
  - 이성체 정보 포함 InChIKey로 통일
    ↓
[강도 정규화]
  - 모든 스펙트럼: 상대 강도값으로 정규화
  - 기기 유형·충돌 에너지 표준화
```

**Step 3: 품질 검증**
- 각 fold의 메타데이터 속성 분포 시각화로 균형 확인
- Spectrum simulation challenge: 모든 메타데이터가 있는 서브셋만 사용
- 공개 저장소에서 코드·데이터 완전 공개로 재현성 보장
- MS 전문성 없이도 사용 가능한 전처리 자동화

**Step 4: 데이터셋 구성 및 공개**
- **MCES(Maximum Common Edge Subgraph) 기반 분할**: 분자 그래프 간 편집 거리를 기준으로 클러스터링 → Tanimoto > 0.85 근사 중복 누출 차단
- StratifiedGroupKFold로 Train / Validation / Test 3-fold 분할
- 스펙트럼 수: Train >> Validation > Test (불균형 방지)
- GitHub: [https://github.com/pluskal-lab/MassSpecGym](https://github.com/pluskal-lab/MassSpecGym)
- HuggingFace: [https://huggingface.co/datasets/roman-bushuiev/MassSpecGym](https://huggingface.co/datasets/roman-bushuiev/MassSpecGym)

## Input (입력)
### 데이터 구성 현황
| 항목 | 규모 |
|---|---|
| 전체 MS/MS 스펙트럼 수 | **231,000+** |
| 고유 분자 구조 수 | **29,000+** |
| 출처 | MoNA, MassBank, GNPS + in-house |
| 분자 크기 | 소분자 (< ~1,000 Da) |

### 세 가지 챌린지
| 챌린지 | 입력 | 출력 | 추가 변형 |
|---|---|---|---|
| **De novo 분자 생성** | MS/MS 스펙트럼 | 분자 구조 (SMILES) | 화학식 제공 버전(보너스) |
| **분자 검색** | MS/MS 스펙트럼 | 후보 DB에서 순위 목록 | 화학식 제공 버전(보너스) |
| **스펙트럼 시뮬레이션** | 분자 구조 (SMILES) | MS/MS 스펙트럼 | 화학식 제공 버전(보너스) |

### 제공 필드
| 필드명 | 설명 |
|---|---|
| `mzs` | m/z 값 배열 (MS/MS 피크) |
| `intensities` | 각 피크 강도 (정규화) |
| `smiles` | 분자 구조 (SMILES 형식) |
| `inchi` | InChI 식별자 |
| `inchikey` | InChIKey (이성체 포함) |
| `precursor_mz` | 전구체 m/z |
| `adduct` | 이온화 adduct 유형 |
| `collision_energy` | 충돌 에너지 |
| `instrument_type` | 기기 유형 |

### 피처화 방법 (ML 벤치마크 전용)
| 방법 | 원리 | 적용 챌린지 |
|---|---|---|
| **Morgan fingerprint** | 분자 서브구조를 비트 벡터(2048-bit, radius=2)로 표현 | 분자 검색, 유사도 계산 |
| **Tanimoto 유사도** | 두 분자 간 공유 비트 비율 (0~1). 1=동일 분자 | 검색 정확도 평가, 구조 유사도 |
| **MCES 거리** | 최대 공통 엣지 서브그래프 편집 거리 | 데이터 분할, de novo 생성 평가 |
| **Cosine 유사도 (스펙트럼)** | 두 MS/MS 스펙트럼의 코사인 유사도 | 스펙트럼 시뮬레이션 평가 |

### 분할 방법
**MCES 기반 분할 (Random 분할이 아님)**:
- MCES 거리를 기준으로 분자를 클러스터링 (distance_threshold=10)
- StratifiedGroupKFold: 동일 클러스터 내 분자는 같은 fold에 배치
- → Tanimoto > 0.85인 유사 분자가 train/test 동시 출현하는 데이터 누출 방지
- 기존 2D InChIKey 기반 분할의 누출 문제를 해결한 핵심 기여

## Output (출력 / 정답 형식)
| 챌린지 | 출력 형태 | 주요 평가 지표 |
|---|---|---|
| De novo 생성 | SMILES 문자열 | Top-k accuracy, MCES 거리, Tanimoto 유사도 |
| 분자 검색 | 순위 목록 | Hit rate @ rank k (HR@k), Top-1 Tanimoto 유사도 |
| 스펙트럼 시뮬레이션 | m/z + intensity 배열 | Cosine 유사도, Top-1 retrieval accuracy |

### 벤치마크된 모델 목록
| 모델 | 유형 | 간략 설명 |
|---|---|---|
| **FraGNNet** | GNN (fragmentation DAG) | ICEBERG 기반 fragmentation graph 신경망, spectrum simulation SOTA (31.93%) |
| **ICEBERG** | GNN (fragmentation DAG) | Goldman et al., 57.8% cosine similarity, forward spectrum simulation SOTA |
| **MIST** | Transformer | 분자 fingerprint 예측으로 검색; 화학식 어노테이션 활용 시 추가 성능 향상 |
| **CSI:FingerID** | SVM / fingerprint | 전통적 MS/MS 검색 방법, fingerprint 기반 |
| **DiffMS** | Diffusion + MIST | fingerprint 예측 후 그래프 diffusion으로 구조 생성; de novo top-1 2.30% |
| **MARASON** | GNN + Neural Graph Matching | Wang et al. 2025, spectrum simulation 34.03% (+6%) |
| **MassSpecGym baseline** | Transformer | 논문 자체 제공 baseline, de novo 생성에서 0% top-1 accuracy |

## 예시 문항 (챌린지별)
**[Type 1: 스펙트럼 시뮬레이션]**
- Input: 분자 구조 C₉H₁₁NO₂ (예: 도파민 유도체의 SMILES)
- Task: MS/MS 스펙트럼 (m/z, intensity 배열) 예측
- 평가: 예측 스펙트럼 vs. 실측 스펙트럼의 코사인 유사도

**[Type 2: 분자 검색]**
- Input: 측정 MS/MS 스펙트럼 (m/z=178.0, intensity 패턴)
- Task: 29k 후보 분자 DB에서 올바른 분자 구조 순위 매기기
- 평가: HR@1, HR@5, HR@10

**[Type 3: De novo 분자 생성]**
- Input: 측정 MS/MS 스펙트럼 + (보너스: 화학식 C₁₀H₁₃NO)
- Task: 스펙트럼만으로 분자 SMILES 생성
- 평가: 예측 SMILES의 2D InChIKey == 정답 InChIKey

## 주요 평가 결과
### 스펙트럼 시뮬레이션 (Top-1 retrieval accuracy)
| 모델 | Top-1 acc | 비고 |
|---|---|---|
| MassSpecGym baseline | ~0% | Transformer baseline |
| FraGNNet | 31.93% | 이전 SOTA |
| **MARASON** (Wang et al. 2025) | **34.03%** | +6% 상대 향상 |
| ICEBERG | 57.8% cosine sim | 화학식 정보 활용 버전 |

### De novo 분자 생성 (Top-1 accuracy)
| 모델 | Top-1 acc | 비고 |
|---|---|---|
| Baseline Transformer | 0% | 논문 기본 baseline |
| DiffMS (Bohde et al. 2025) | 2.30% | Diffusion 기반 현재 SOTA |

## 한계점
- **소분자 편향**: 공개 MS 라이브러리 특성상 소분자(< ~1,000 Da) 중심
- **양성 이온 모드 편향**: [M+H]⁺ 등 양성 이온화 adduct 과다 대표
- **기기 이질성**: 다양한 기기·충돌 에너지 설정이 스펙트럼 패턴에 영향
- **De novo 생성 난이도**: 현재 최고 성능 모델도 2.30% → 실용화 요원
- **이성체 구분 한계**: 동일 2D 구조의 입체이성체 구분이 MS/MS로 불가능한 경우 존재

## 관련 정보
- **원 논문 링크 (NeurIPS 2024 공식)**: [https://proceedings.neurips.cc/paper_files/paper/2024/hash/c6c31413d5c53b7d1c343c1498734b0f-Abstract-Datasets_and_Benchmarks_Track.html](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c6c31413d5c53b7d1c343c1498734b0f-Abstract-Datasets_and_Benchmarks_Track.html)
- **arXiv**: [https://arxiv.org/abs/2410.23326](https://arxiv.org/abs/2410.23326)
- **GitHub**: [https://github.com/pluskal-lab/MassSpecGym](https://github.com/pluskal-lab/MassSpecGym)
- **HuggingFace**: [https://huggingface.co/datasets/roman-bushuiev/MassSpecGym](https://huggingface.co/datasets/roman-bushuiev/MassSpecGym)
- **이 벤치마크를 사용한 RAG 논문**: Wang, Wang, Manjrekar, Coley (2025) — MARASON, ICML 2025
