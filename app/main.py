from app.graph.workflow import build_graph

if __name__ == "__main__":
    graph = build_graph()
    result = graph.invoke({})

    print("\n✅ FINAL RESULT")
    print("Risk Level:", result["risk_level"])