# AIVC - AI Virtual Company

핸드폰에서 명령을 내리면 AI 팀장이 작업을 분해하고, AI 팀원들이 병렬로 수행한 뒤 최종 보고서를 올려주는 시스템.

## 구조

```
[사장 (폰)] → 명령 → [AI 팀장] → 작업 분배 → [AI 팀원들 (병렬)]
                                                    ↓
                                            최종 보고서 → [사장]
```

## 팀원 역할
- **researcher**: 정보 조사, 분석
- **writer**: 문서, 이메일, 보고서 작성
- **coder**: 코드 작성, 기술 구현
- **planner**: 일정 관리, 계획 수립

## 실행

```bash
# 백엔드
cd backend
pip install -r requirements.txt
cp .env.example .env  # ANTHROPIC_API_KEY 설정
uvicorn app.main:app --reload

# 프론트엔드
cd frontend
npm install
npm start
```

## 기술 스택
- **Backend**: Python, FastAPI, SQLite
- **Frontend**: React (PWA)
- **AI**: Claude API (Anthropic)
