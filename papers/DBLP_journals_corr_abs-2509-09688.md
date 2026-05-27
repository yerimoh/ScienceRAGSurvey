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

> arXiv 2509.09688 | 2025 | Method | physics
> Brookhaven National Laboratory (STAR / PHENIX / sPHENIX / RHIC DAPP)

## 한 줄 요약
25년간 운영된 브룩헤이븐 RHIC 가속기의 **약 1 EB 데이터 + 600편 이상 논문 + 메일링 리스트 등 암묵적 지식**을 영구 보존하기 위해, **MCP(Model Context Protocol) 기반 RAG 어시스턴트**(DAPP)를 구축. ChromaDB + vLLM/Llama3.3·Mistral-Large·LlamaCpp/Ollama로 on-premise 인프라 구성, 비공개 내부 메일링 리스트까지 인용 가능.

## 제작 배경
**기존 방법의 한계**
- 25년간 RHIC가 축적한 STAR/PHENIX/sPHENIX 실험 노하우는 내부 메일링 리스트·기술 노트·구형 PostScript 등 분산 형태로 흩어져 있어 유실 위험
- ChatGPT/Gemini/Claude 등 상용 LLM은 공개 데이터만 학습 → 비공개 내부 컨텍스트(디버깅 기록, 운영 노트 등) 접근 불가
- 협업 정책(public / collaboration-restricted / controlled) 차등으로 인해 단일 클라우드 SaaS 사용 불가

**왜 이 시스템이 필요했는지**
- "오늘날의 대학원생이 20년 전에 개발된 방법론을 이해해야 할 수 있다"는 시계열 문제 해결 필요
- 2025년 RHIC 운영 종료에 맞춰 **EIC(Electron-Ion Collider) 후속 실험**으로 지식 전수
- 출판 전 내부 자료를 외부에 노출하지 않으면서도 자연어 질의 가능한 인터페이스 제공

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — Recursive Multi-Format Web-Content Extraction (Fig. 2.1)
  Seed URL → BeautifulSoup + requests로 HTML 순회
  dynamic filter / blacklist (calendars, login 페이지 차단)
  파일 확장자별 전용 파서:
  ┌─ HTML       : nav 제거 → 본문 + 하이퍼링크 파싱
  ├─ PDF        : Marker (ML-based PDF→Markdown)
  ├─ DOC/PPT    : LibreOffice 변환
  └─ PS/EPS     : Ghostscript로 PDF 변환 후 Marker

Step 2 — 텍스트 정제 + 메타데이터 헤더 부착
  source URL, page title, timestamp 추가
  통계 로깅(redirect/filter/extension 빈도)

Step 3 — 벡터 임베딩 (ChromaDB)
  RHIC 기술 노트 · 컨퍼런스 슬라이드 · 코드 스니펫 · SW 문서
  embedded into searchable ChromaDB

Step 4 — MCP 오케스트레이션 (FastAPI-MCP)
  /ask 요청에 JSON 헤더 부착:
    - ordered stack of models
    - max context budget per stage
    - security tier (caller credentials 기반)
  단계별 컨텍스트 분리: retrieval → summarization
                       → inference → evaluation
  보안 티어별 라우팅 (public/collaboration-restricted/controlled)

Step 5 — 멀티 엔진 추론 비교 (Fig. 3.1)
  vLLM      : 멀티-GPU 처리량 ↑, 80%+ utilization 유지
  LlamaCpp  : 1-GPU 처리량 ↑, 4-GPU에서 21% utilization로 급감
  Ollama    : GPU 수 증가 시 처리량·utilization 모두 감소
  HW: A6000 → A100 → H100 순으로 throughput 확장
```

## Input (입력)
- **수집 대상**: RHIC 내부 collaboration website, 아카이브, 메일링 리스트 (HTML/PDF/PS/DOCX/PPTX)
- **사용자 질의**: 자연어 (`/ask` 엔드포인트)
- **보안 컨텍스트**: SSO 인증, RBAC, 데이터 분류 (public / collaboration-restricted / controlled)

## Output (출력)
- 검색 컨텍스트로 LLM이 생성한 응답 (Llama3.3-70B / Mistral-Large-2411 / ChatGPT o3 비교)
- 출처 문서 인용 (메일링 리스트 / arXiv / 내부 기술 노트)
- 향후: AES-256 at rest, TLS 1.3 in transit, audit log

## 예시 문항 (논문 본문 4. Benchmarking 섹션 직접 인용)

본 시스템은 STAR 전문가들이 작성한 내부 벤치마크 질의로 평가됨. 본문에 명시된 두 가지 verbatim Q:

### 📘 STAR 검출기 운영 질의 ①
> **Q**: "How are space charge effects considered in the STAR experiment?"
> **평가 방식**: 도메인 전문가들이 작성한 ground-truth 답변과 LLM 응답을 정성 비교

### 📘 STAR 검출기 운영 질의 ②
> **Q**: "What is the TOF resolution in STAR experiment?"
> **평가 방식**: 동일 (전문가 reference vs LLM 생성)

### 📘 평가 시스템 비교 (본문 그대로)
> "Llama3.3 model was noted for its concise and detailed narrative, whereas Mistral was similarly precise but slightly more verbose. In contrast, ChatGPT o3 adopted a more pedagogical, verbose style that, while comprehensive, included extraneous details."
>
> "Llama3.3 and Mistral models successfully and quickly retrieved context from internal collaboration mailing lists, which are inaccessible to public-facing commercial LLMs."

## 주요 평가 결과

**LLM 비교 (정성 평가, 본문 4장)**

| LLM | 구동 환경 | 핵심 평가 결과 |
|---|---|---|
| **Llama3.3-70B + RAG** | 로컬 vLLM | 정확·간결, **내부 메일링 리스트 인용 성공** |
| **Mistral-Large-2411 + RAG** | 로컬 | 정확하나 약간 장황 |
| ChatGPT o3 (baseline) | 상용 SaaS | arXiv / ResearchGate 등 **공개 자료만** 인용, 내부 디버깅 기록 미접근 |

**추론 엔진 처리량 (Fig. 3.1, 정량)**

| 엔진 | 1-GPU 처리량 | 4-GPU 활용률 | 디자인 철학 |
|---|---|---|---|
| vLLM | 중간 | **>80% 유지** | parallel-first |
| LlamaCpp | **최고** | 21%로 급감 | memory distribution-first |
| Ollama | 중간 | 점진적 감소 | balanced |

> HW 세대별: H100 > A100 > A6000 (모든 엔진 공통)

## 핵심 기여
1. **퍼블릭 챗봇이 접근할 수 없는 비공개 메일링 리스트 + 비공식 디스커션을 LLM 지식 베이스로 통합**
2. **MCP 채택**: 검색·요약·추론·평가 단계를 독립 컨텍스트로 분리 → 모니터링·설명 가능성 ↑
3. **3-engine benchmark**: vLLM/LlamaCpp/Ollama 처리량·utilization 정량 비교 (Fig. 3.1)
4. **STAR 사용 사례 → EIC 일반화 가능 템플릿** 제시

## 한계점
- 평가가 **정성 비교(qualitative)** 위주, 정량 IR 지표(P@k, MRR) 부재
- Public / collaboration-restricted / controlled 권한 분리·RBAC 완전 구현 진행 중
- 외부 최신 출판물(API, RSS feed) ↔ 로컬 DB 자동 동기화 미구현
- 평가용 인사이더-레벨 질문 세트 규모 미공개

## 관련 정보
- **논문**: [arXiv:2509.09688](https://arxiv.org/abs/2509.09688) (NYSDS 2025)
- **발표**: New York Scientific Data Summit 2025
- **관련 도구**: ChromaDB · Marker · FastAPI-MCP · vLLM · LlamaCpp · Ollama
- **후속 비전**: EIC 실험 통합 (논문 결론부)
