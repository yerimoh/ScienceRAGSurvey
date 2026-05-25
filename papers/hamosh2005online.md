---
title: "Online Mendelian Inheritance in Man (OMIM), a knowledgebase of human genes and genetic disorders"
bib_key: "hamosh2005online"
year: 2005
domain: medical
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gki033
---
# Online Mendelian Inheritance in Man (OMIM), a knowledgebase of human genes and genetic disorders

hamosh2005online | 2005 | Nucleic Acids Research | dataset | [medical] | [paper](https://doi.org/10.1093/nar/gki033)

**DB**: OMIM (Online Mendelian Inheritance in Man)
**DB size**: 15,593개 항목 (2004년 9월 기준); 유전자 9,816개, 표현형 5,777개
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: OMIM 웹사이트 / NCBI Entrez 통합 검색

> Nucleic Acids Research | 2005 | dataset | medical
#### 📌 한 줄 요약
존스홉킨스대학교 McKusick-Nathans 연구소가 관리하고 NCBI가 배포하는 인간 유전자·유전 질환의 권위 있는 카탈로그로, 2004년 기준 15,593개 항목과 12,715개의 대립형질 변이를 수록한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- Victor McKusick의 1966년 인쇄물 "Mendelian Inheritance in Man(MIM)"이 기원이나, 인쇄 갱신 주기로는 급증하는 유전 발견을 따라잡기 어려웠다
- 인쇄·CD-ROM 형식으로는 일일 문헌 업데이트 및 외부 DB 링크 기능이 불가했다

**이 시스템이 필요한 이유**
- 유전체 혁명으로 매일 새로운 유전자-질환 연관이 보고되어 실시간 온라인 갱신이 필수가 됐다
- 임상 의사와 연구자가 단일 플랫폼에서 유전자·표현형·문헌·시퀀스 DB를 교차 검색해야 했다

#### 🔨 시스템 구성
각 OMIM 항목은 고유한 6자리 MIM 번호로 식별되며 유전자(별 기호), 표현형, 유전자-표현형 관계를 기술한다.
- **MIM 번호 체계**: 앞자리로 항목 유형 구분 (1xxxx = 상염색체 우성, 2xxxx = 상염색체 열성, 3xxxx = X-연결 등)
- **Allelic Variant 섹션**: 각 항목 내 임상적으로 중요한 돌연변이 기재 (2004년 기준 1,651개 항목에 12,715개 변이)
- **Clinical Synopsis**: 표현형별 임상 특징 요약 (4,500개 이상)
- **Morbid Map**: 유전자-질환 매핑 알파벳 순 목록

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | omim.org — 무료 검색; 개인·비영리 사용 |
| NCBI Entrez | PubMed, Gene, OMIM 통합 검색 연결 |
| FTP 다운로드 | 상업적 사용 시 별도 라이선스 필요 |

#### 📤 제공 데이터 형식
- MIM 번호별 텍스트 항목 (유전자 기술, 표현형, 임상 시놉시스)
- 대립형질 변이 목록 (Allelic Variant 섹션)
- 유전자-표현형 매핑 테이블 (Morbid Map)
- NCBI Gene, sequence DB, PubMed 상호 링크

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 전체 항목 수 | **15,593개** (2004년 9월 기준) |
| 유전자 항목 (분자 서열 확인) | **9,816개** |
| 표현형/질환 항목 | **5,777개** |
| 대립형질 변이 수 | **12,715개** (1,651개 항목) |
| 임상 시놉시스 수 | **4,500개 이상** |
| 매핑된 질환 수 | **3,659개** (2,558개 유전자 좌위에 분포) |
| 분자 기전 확인 질환 | **2,563개** |
| 일일 고유 방문자 | **약 8,500명** |
| 일일 쿼리 수 | **약 100,000건** |
| 월간 신규 항목/업데이트 | 신규 약 70개, 업데이트 약 600건 |

#### ⚠️ 한계점
- 멘델 유전 질환 중심: 복합(다유전자·환경) 질환은 포함 범위가 제한적
- 상업적 재배포·활용 시 별도 라이선스 협의 필요
- 텍스트 중심 서술로 구조화된 쿼리(SPARQL 등)에 직접 활용 어려움

## 관련 정보
- **논문**: [Hamosh et al., Nucleic Acids Research 2005](https://doi.org/10.1093/nar/gki033)
