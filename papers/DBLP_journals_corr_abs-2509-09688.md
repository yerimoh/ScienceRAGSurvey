---
notion_id: 355f2dcd-4912-819f-b9a3-f56eb8671fdb
title: AI-Powered Assistant for Long-Term Access to RHIC Knowledge
bib_key: DBLP:journals/corr/abs-2509-09688
year: 2025
domain: physics
type: Method
venue: New York Scientific Data Summit 2025
paper_link: https://arxiv.org/abs/2509.09688
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# AI-Powered Assistant for Long-Term Access to RHIC Knowledge

> arXiv | 2025 | Method | physics
## 📌 한 줄 요약
25년간 운영된 브룩헤이븐 국립 연구소 RHIC 가속기의 방대한 실험 지식과 비공개 내부 문서를 영구 보존하고 쿼리할 수 있도록 설계된 MCP(Model Context Protocol) 기반 RAG 어시스턴트 시스템.
## 🎯 연구 배경 및 동기
- **기존 방법의 한계점**: 대형 입자 물리 실험실에서는 기술 노트, 실험 노하우, 검출기 관련 심층 지식 등 방대한 "암묵적 지식(Tacit Knowledge)"이 내부 메일링 리스트와 분산된 레거시 문서 형태로 흩어져 있어 유실 위험이 높음. 상용 LLM(ChatGPT 등)은 이러한 비공개 내부망 데이터에 접근할 수 없음.
- **이 연구가 필요한 이유**: RHIC 가속기가 2025년 운영을 종료함에 따라, 약 1 ExaByte에 달하는 데이터와 25년간 누적된 실험적 지식을 향후 세대(EIC 실험 등)가 원활하게 검색하고 재현할 수 있는 차세대 지식 보존 프레임워크(DAPP)가 절실히 요구됨.
## 🏗️ 시스템 아키텍처
1. **Data Harvesting**: Custom Web Scraper가 내부 웹사이트, 아카이브, 메일링 리스트를 순회하며 다양한 확장자(HTML, PDF, DOCX, PS 등) 다운로드.
2. **Data Extraction & Cleaning**: Marker(ML 기반 PDF 파싱), LibreOffice 등을 사용해 구조 보존형 Markdown으로 변환.
3. **Indexing**: ChromaDB를 이용해 추출된 텍스트를 임베딩 벡터로 변환하여 저장.
4. **MCP Orchestration**: 사용자 쿼리가 인입되면 Model Context Protocol 래퍼가 쿼리를 분석하고 검색 백엔드로 라우팅.
5. **Generation**: 검색된 컨텍스트를 융합(fusion)하여 Llama3.3 또는 Mistral 기반 엔진이 최종 답변 및 출처 인용 내역 생성.
## 🔑 핵심 모듈 상세 설명
- **Recursive Multi-Format Web-Content Extraction Framework**: ML 모델인 Marker를 도입해 수식 및 레이아웃 유지율을 기존 파서 대비 획기적으로 개선. PDF뿐 아니라 구형 PostScript 파일까지 처리.

| 모듈/도구명 | 연동 방식 및 목적 |
| Marker Library | ML을 통해 복잡한 표/수식 포함 PDF 문서를 시맨틱 손실 없이 Markdown으로 변환 |
| ChromaDB | 정제된 내부 기술 문서 및 메일링 리스트 아카이브를 벡터화하여 Semantic Search 제공 |
| MCP (Model Context Protocol) | 검색, 요약, 추론 단계를 독립된 컨텍스트로 분리하여 실행 로직과 배포 환경 디커플링 |

## 🧪 실험 및 평가
- **평가 데이터**: 다년간 경험을 갖춘 STAR 실험 도메인 전문가들이 직접 작성한 내부 질문 세트.
- **비교 모델 결과**:
| LLM | 구동 환경 | 질적 평가 결과 |
| Llama3.3-70B (RAG) | 로컬 vLLM | 정확하고 간결. 내부 메일링 리스트(비공개 자료) 성공적으로 인용. |
| Mistral-Large-2411 (RAG) | 로컬 | 정확하나 약간 장황한 텍스트 톤. |
| ChatGPT o3 (Baseline) | 상용 서비스 | 퍼블릭 데이터에만 의존하여 내부 심층 컨텍스트(디버깅 기록 등) 확보 실패. |

## 💡 핵심 기여
1. 퍼블릭 AI 챗봇이 도달할 수 없는 **조직 내부의 암묵적 학술 지식과 문제 해결 과정(메일링 리스트 등)을 LLM 지식 베이스로 통합**함.
2. Model Context Protocol(MCP)을 선도적으로 채택하여 RAG 파이프라인 각 단계의 모니터링 및 설명 가능성을 극대화함.
3. vLLM, LlamaCpp, Ollama 등 다양한 추론 엔진의 병렬 처리 확장성을 실증적으로 비교 분석함.
## ⚠️ 한계점
- Public / Collaboration-restricted / Controlled 데이터의 권한이 복잡하여 역할 기반 접근 제어(RBAC) 및 보안 통합(SSO, AES-256) 모듈 고도화가 추가로 필요함.
- 외부 최신 출판물(API, RSS 피드 등)과 로컬 DB 간의 자동 동기화 기능은 아직 구현 전 단계임.
## 🔗 관련 연구 및 관련 정보
- 논문 링크: [https://arxiv.org/abs/2509.09688](https://arxiv.org/abs/2509.09688)
- 오픈 벤치마크 미활용. 향후 고차원 도메인 특화 성능 평가 프레임워크 공개 예정.
