from typing import TypedDict,Optional

class SOCState(TypedDict):
    alert: dict
    risk_score: float
    shap_summary: Optional[str]
    investigation_notes: Optional[str]
    decision: Optional[str]
    report: Optional[str]