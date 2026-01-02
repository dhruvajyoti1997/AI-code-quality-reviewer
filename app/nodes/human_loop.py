def human_loop_node(state):
    print("\n⚠️ HUMAN REVIEW REQUIRED ⚠️")
    print("Current Risk:", state["risk_level"])
    print("\nAnalysis Summary:\n", state["analysis"])

    feedback = input(
        "\nExplain WHY this design was chosen "
        "(constraints, performance, business logic):\n"
    )

    return {
        "human_feedback": feedback
    }