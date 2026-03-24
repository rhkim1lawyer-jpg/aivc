import anthropic


ROLE_PROMPTS = {
    "researcher": "당신은 리서치 전문가입니다. 주어진 주제에 대해 체계적으로 조사하고 핵심 정보를 정리하세요.",
    "writer": "당신은 문서 작성 전문가입니다. 명확하고 전문적인 문서를 작성하세요.",
    "coder": "당신은 시니어 개발자입니다. 깔끔하고 동작하는 코드를 작성하세요. 코드 블록으로 감싸서 제공하세요.",
    "planner": "당신은 프로젝트 매니저입니다. 실행 가능한 구체적인 계획과 일정을 수립하세요.",
}


async def execute_task(assignee: str, description: str) -> str:
    client = anthropic.AsyncAnthropic()
    system = ROLE_PROMPTS.get(assignee, "주어진 작업을 성실히 수행하세요.")

    response = await client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=system,
        messages=[{"role": "user", "content": description}],
    )

    return response.content[0].text
