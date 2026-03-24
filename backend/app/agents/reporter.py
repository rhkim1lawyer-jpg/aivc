import anthropic


SYSTEM_PROMPT = """당신은 보고 담당자입니다.
팀원들이 수행한 작업 결과를 취합하여 사장님께 깔끔한 최종 보고서를 작성하세요.

보고서 형식:
1. 한줄 요약
2. 각 작업별 핵심 결과
3. 종합 결론 및 다음 단계 제안"""


async def create_report(original_command: str, results: list[dict]) -> str:
    client = anthropic.AsyncAnthropic()

    results_text = "\n\n".join(
        f"### [{r['assignee']}] {r['title']}\n{r['result']}"
        for r in results
    )

    prompt = f"""원래 명령: {original_command}

팀원들의 작업 결과:
{results_text}

위 결과를 바탕으로 최종 보고서를 작성하세요."""

    response = await client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.content[0].text
