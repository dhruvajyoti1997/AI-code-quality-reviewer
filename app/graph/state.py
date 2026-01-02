from typing import List, Optional, TypedDict

class ReviewState(TypedDict):
    files : List[str]
    code_chunks: List[str]
    retrieved_context: str
    analysis: str
    risk_level: Optional[str]
    human_feedback: Optional[str]