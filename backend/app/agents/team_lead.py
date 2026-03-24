import anthropic
import json


SYSTEM_PROMPT = """당신은 AI 팀장입니다. 사용자(사장님)의 명령을 받아 하위 작업으로 분해합니다.

각 작업에 적합한 팀원을 배정하세요:
- researcher: 정보 조사, 검색, 분석
- writer: 문서 작성, 이메일, 보고서
- coder: 코드 작성, 기술 구현
- planner: 일정 관리, 계획 수립

반드시 아래 JSON 형식으로만 응답하세요:
{
  "plan": "전체 실행 계획 요약",
  "subtasks": [
    {
      "id": 1,
      "title": "작업 제목",
      "assignee": "researcher|writer|coder|planner",
      "description": "팀원에게 전달할 구체적인 지시사항"
    }
  ]
}"""


async def decompose_command(message: str) -> dict:
    client = anthropic.AsyncAnthropic()

    response = await client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": message}],
    )

    text = response.content[0].text

    # JSON 블록 추출
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0]
    elif "```" in text:
        text = text.split("```")[1].split("```")[0]

    return json.loads(text.strip())
