from app.llm.llm_provider import get_llm
from pathlib import Path
PROMPT = Path("app/prompts/classification_prompt.txt").read_text()

def classify_risk_node(state):
    prompt = PROMPT.format(analysis = state["analysis"])
    response = get_llm.invoke(prompt)

    risk = response.content.strip().upper()

    return {
        "risk_level": risk
    }