from langgraph.graph import StateGraph
from app.graph.state import ReviewState
from app.nodes.fetch_github_code  import fetch_github_code
from app.nodes.retrieve_context import retrieve_context_node
from app.nodes.analyze_code import analyze_code_node
from app.nodes.human_loop import human_loop_node
from app.nodes.classify_risk import classify_risk_node

def build_graph():
    graph = StateGraph(ReviewState)
    graph.add_node("fetch_code", fetch_github_code)
    graph.add_node("retrieve", retrieve_context_node)
    graph.add_node("analyze", analyze_code_node)
    graph.add_node("classify", classify_risk_node)
    graph.add_node("human", human_loop_node)

    graph.set_entry_point("fetch_code")

    graph.add_edge("fetch_code", "retrieve")
    graph.add_edge("retrieve", "analyze")
    graph.add_edge("analyze", "classify")
    graph.add_conditional_edges(
        "classify",
        lambda state: state["risk_level"],
        {
            "LOW": None,
            "MEDIUM": "human",
            "HIGH": "human"
        }
    )

    graph.add_edge("human", "analyze")
    return graph.compile()

