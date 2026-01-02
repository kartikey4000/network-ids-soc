from autogen import AssistantAgent, UserProxyAgent
from graph.state import SOCState

def investigate(state: SOCState) -> SOCState:
    if state["decision"] == "IGNORE":
        return {
            **state,
            "investigation_notes": "No investigation required."
        }

    llm_config = {
        "model": "gpt-4o-mini",
        "temperature": 0.2,
    }

    analyst = AssistantAgent(
        name="SOC_Analyst",
        llm_config=llm_config
    )

    system = UserProxyAgent(
        name="System",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=1,
        code_execution_config=False
    )

    prompt = f"""
Alert: {state['alert']}
Risk Score: {state['risk_score']}
Reason: {state['shap_summary']}
Decision: {state['decision']}

Write a short SOC analyst investigation summary.
"""

    system.initiate_chat(analyst, message=prompt)

    return {
        **state,
        "investigation_notes": analyst.last_message()["content"]
    }
