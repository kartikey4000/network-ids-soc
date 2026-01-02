from graph.state import SOCState

def decide(state: SOCState) -> SOCState:

    score = state["risk_score"]

    if score >= 0.9:
        decision = "Block"
    elif score >= 0.4:
        decision = "MONITOR"
    else:
        decision = "IGNORE"

    return {
        **state,
        "decision": decision
    }

    