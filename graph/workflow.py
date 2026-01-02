from langgraph.graph import StateGraph
from graph.state import SOCState
from agents.ml_threat_agent import threat_analysis
from agents.decision_agent import decide
from agents.inverstigation_agent import investigate


def dummy_investigate(state: SOCState):
    return state


def dummy_report(state: SOCState):
    return state

builder = StateGraph(SOCState)

builder.add_node("threat",threat_analysis)
builder.add_node("investigate", investigate)
builder.add_node("decide", decide)
builder.add_node("report", dummy_report)

builder.set_entry_point("threat")
builder.add_edge("threat", "decide")
builder.add_edge("decide", "investigate")
builder.add_edge("investigate", "report")

graph = builder.compile()