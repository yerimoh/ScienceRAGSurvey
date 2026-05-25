---
title: "MATLAB and Simulink"
bib_key: "matlabsimulink"
year: 1984
domain: general
type: dataset
venue: MathWorks (Commercial Software)
paper_link: https://www.mathworks.com
---
# MATLAB and Simulink

matlabsimulink | 1984 | MathWorks (Commercial Software) | dataset | [general] | [website](https://www.mathworks.com)

**DB**: MATLAB 내장 수치 알고리즘 라이브러리, Simulink 블록다이어그램 라이브러리 및 파라미터베이스 (Aerospace, Control System, Signal Processing Toolbox 등)
**DB size**: N/A (라이선스 소프트웨어, 공개 수치 없음)
**DB Open/Private**: Subscription (상용 라이선스; 학술 할인 있음)
**Modality**: Tabular, Code
**Retriever**: N/A (K4 상업용 계산 환경 — 직접 queryable API 없음)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: MATLAB / Simulink (MathWorks)

> MathWorks | 1984 | dataset | general
#### 📌 한 줄 요약
MathWorks가 1984년(MATLAB)/1990년(Simulink) 출시한 수치 계산·시뮬레이션 환경으로, 제어공학, 신호처리, 항공우주, 자율주행 등 광범위한 공학 도메인의 전문 지식이 Toolbox 형태로 캡슐화되어 산업 및 학술 표준으로 사용된다.

#### 🎯 개발/구축 배경
**기존 계산 도구의 한계**
- 1970~1980년대 공학 계산은 FORTRAN/BASIC 코딩이 필요하여 비수학 전공자에게는 장벽이 높음
- 제어 시스템 설계, 신호처리 알고리즘 검증을 위한 표준화된 계산·시각화 환경이 없었음

**MATLAB/Simulink의 위치**
- MATLAB: 행렬 기반 수치 계산 및 데이터 분석의 사실상 표준 (특히 제어·신호처리 분야)
- Simulink: 블록다이어그램 기반 동적 시스템 시뮬레이션; 제어 시스템, 파워트레인, 항공전자 설계에서 자동코드생성(AutoCode)까지 활용

#### 🔨 시스템 구성
- **MATLAB Core**: 행렬 연산, 최적화, 통계, 기계학습 함수 라이브러리
- **Simulink**: 연속/이산 시스템 모델링용 블록다이어그램 환경 + Stateflow(유한상태기계)
- **Toolboxes**: Control System, Signal Processing, Aerospace, Robotics, Deep Learning, Phased Array 등 100개 이상
- **Embedded 지식**: 각 Toolbox에 도메인 전문 알고리즘 파라미터와 레퍼런스 모델 내장

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| MATLAB 인터프리터 | 인터랙티브 커맨드 창 및 스크립트 실행 |
| Simulink GUI | 블록다이어그램 기반 모델 구성 및 시뮬레이션 |
| MATLAB Engine API | Python/C/C++/Java에서 MATLAB 엔진 호출 |
| MATLAB Online | 클라우드 기반 웹 환경 |

#### 📤 제공 데이터 형식
- 수치 배열, 구조체, 테이블 (.mat, .csv, Excel 출력)
- Simulink 시뮬레이션 결과 (.slx, .mat 시계열 데이터)
- 자동 코드 생성 결과 (C/C++, HDL, PLC 코드)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| MATLAB 최초 출시 | 1984 |
| Simulink 최초 출시 | 1990 |
| 지원 Toolbox 수 | 100개 이상 (도메인별 전문 라이브러리) |
| 공개 데이터베이스 규모 | 비공개 (상용 라이선스) |

#### ⚠️ 한계점
- Toolbox에 캡슐화된 알고리즘 파라미터와 레퍼런스 데이터는 외부 RAG 시스템에서 직접 접근·질의 불가
- Python(NumPy/SciPy) 생태계로의 전환이 일부 분야에서 진행 중이나 제어·항공 분야의 레거시 코드 의존성은 여전히 강함
- 라이선스 비용 및 플랫폼 종속성이 오픈소스 대안에 비해 단점

## 관련 정보
- **웹사이트**: [MathWorks MATLAB](https://www.mathworks.com/products/matlab.html) / [MathWorks Simulink](https://www.mathworks.com/products/simulink.html)
- **K4 분류**: Embedded in software — 제어·신호처리·항공우주 공학 tacit knowledge가 Toolbox 파라미터베이스에 내장됨
