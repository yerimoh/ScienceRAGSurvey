---
title: "OMIM.org: Online Mendelian Inheritance in Man (OMIM®), an online catalog of human genes and genetic disorders"
bib_key: "amberger2015omim"
year: 2015
domain: medical
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gku1205
---
# OMIM.org: Online Mendelian Inheritance in Man (OMIM®), an online catalog of human genes and genetic disorders

amberger2015omim | 2015 | Nucleic Acids Research | dataset | [medical] | [paper](https://doi.org/10.1093/nar/gku1205)

**DB**: OMIM.org (Online Mendelian Inheritance in Man — 2015 리뉴얼)
**DB size**: 24,000개 이상 항목 (2014년 기준 갱신치); 유전자·표현형·유전자-표현형 관계
**DB Open/Private**: Open (개인·비영리 무료; 상업적 사용은 라이선스)
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: OMIM API / FTP download

> Nucleic Acids Research | 2015 | dataset | medical
#### 📌 한 줄 요약
2015년 리뉴얼된 OMIM.org는 안정적인 6자리 MIM 번호 체계, 유전체 좌위 검색, UMLS·HPO·EoM 연계 임상 시놉시스, REST API 및 FTP 공개 데이터를 제공하는 인간 멘델 유전 질환의 표준 참조 자원이다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 2005년 hamosh2005online 논문 이후 OMIM 항목 수와 사용 방식이 크게 변화했다
- 검색 인터페이스가 노후화되어 게놈 좌위 기반 검색, 표현형 계층 검색이 지원되지 않았다
- 항목 내 어휘가 비표준화되어 HPO, UMLS 등 외부 온톨로지와 연결이 어려웠다

**이 시스템이 필요한 이유**
- 차세대 시퀀싱(NGS) 시대에 임상 유전학자가 변이-표현형 연관을 신속하게 탐색할 인프라가 필요하다
- 계산 기반 유전 분석 도구들이 OMIM 데이터를 자동으로 소비할 수 있는 API가 요구됐다

#### 🔨 시스템 구성
- **MIM 번호 안정성**: 항목 유형별 고유 6자리 번호; 유전자(*), 표현형(#, %, ^) 구분 유지
- **개선된 Clinical Synopsis**: UMLS(통제어휘), Human Phenotype Ontology(HPO), Elements of Morphology(EoM) 용어로 표준화
- **Phenotypic Series**: 유전적 이질성(genetic heterogeneity)을 가진 질환 군을 하나의 시리즈로 묶어 표시
- **MIMmatch**: 신규 OMIM 항목·업데이트 발표 이메일 서비스
- **게놈 좌위 검색**: 염색체 위치·좌위로 OMIM 항목 검색

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| OMIM API | REST API — 항목 조회, 검색; omim.org/api |
| FTP 다운로드 | 전체 데이터셋 다운로드; 학술 연구 무료, 상업적 사용 라이선스 |
| 웹 인터페이스 | omim.org — 향상된 검색 (게놈 좌위, 시소러스 확장 검색어) |

#### 📤 제공 데이터 형식
- MIM 항목 텍스트 (유전자 기술, 대립형질 변이, 임상 시놉시스)
- 표현형 시리즈(Phenotypic Series) 테이블
- HPO 용어 매핑, UMLS CUI 연결
- Morbid Map (유전자-표현형 매핑 테이블)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 항목 총수 | 논문 기재치 미명시 (2014 기준 ~24,000개) |
| API 제공 | ✓ (REST API 공개) |
| FTP 제공 | ✓ (학술 무료) |
| HPO 연계 | ✓ Clinical Synopsis 전면 HPO 용어화 |
| UMLS 연계 | ✓ |
| 운영 기관 | Johns Hopkins University (McKusick-Nathans Institute) |

#### ⚠️ 한계점
- 상업적 사용 시 라이선스 계약 필요 (제약·바이오텍 기업)
- 복합 유전 질환(다유전자, GxE 상호작용)은 커버리지 제한
- API는 배치 처리보다 개별 항목 조회에 최적화; 대규모 자동 파이프라인에는 FTP 다운로드 권장

## 관련 정보
- **논문**: [Amberger et al., Nucleic Acids Research 2015](https://doi.org/10.1093/nar/gku1205)
