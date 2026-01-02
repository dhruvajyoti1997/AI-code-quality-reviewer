from app.llm.llm_provider import get_llm
from pathlib import Path

PROMPT = Path("app/prompts/analysis_prompt.txt").read_text()
HITL_PROMPT = Path("app/prompts/hitl_prompt.txt").read_text()

def analyze_code_node(state):
    human_intent = state.get("human_feedback")
    prompt = PROMPT.format(
        code="\n".join(state["code_chunks"]),
        context=state["retrieved_context"]
    )

    if human_intent:
        prompt = (
            prompt + "\n\n" + HITL_PROMPT.format(human_intent=human_intent)
        )
    response = get_llm.invoke(prompt)
    return {
        "code_analysis": response.content
    }


