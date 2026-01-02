import joblib
import pandas as pd
import numpy as np
from graph.state import SOCState

# Load trained pipeline (Imputer + XGBoost)
MODEL_PATH = "agents/soc_xgboost_unsw_nb15.pkl"
model = joblib.load(MODEL_PATH)

REQUIRED_FEATURES = [
    "dur",

    "sbytes", "dbytes",
    "Spkts", "Dpkts",
    "smeansz", "dmeansz",

    "Sload", "Dload",

    "tcprtt", "synack", "ackdat",

    "Sintpkt", "Dintpkt",
    "Sjit", "Djit",

    "swin", "dwin",

    "ct_state_ttl",
    "ct_flw_http_mthd",
    "is_ftp_login",
    "ct_ftp_cmd",

    "ct_srv_src",
    "ct_srv_dst",
    "ct_dst_ltm",
    "ct_src_ ltm",
    "ct_src_dport_ltm",
    "ct_dst_sport_ltm",
    "ct_dst_src_ltm",

    "is_sm_ips_ports"
]

def apply_training_transforms(x: pd.DataFrame) -> pd.DataFrame:
    """
    Minimal preprocessing — MUST match training logic
    """
    x = x.copy()

    # Replace inf with nan (SimpleImputer handles this)
    x.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Force numeric
    for col in x.columns:
        x[col] = pd.to_numeric(x[col], errors="coerce")

    return x

def threat_analysis(state: SOCState) -> SOCState:
    """
    ML-based threat detection agent using UNSW-NB15
    """

    alert = state["alert"]

    # 🔒 Schema validation
    missing = [f for f in REQUIRED_FEATURES if f not in alert]
    if missing:
        raise ValueError(f"Alert missing required features: {missing}")

    # 🧪 Build feature vector
    x = pd.DataFrame([{f: alert[f] for f in REQUIRED_FEATURES}])

    print("\n🔎 Raw Alert Features:")
    print(x)

    # Apply SAME preprocessing as training
    x = apply_training_transforms(x)

    print("\n🧼 Cleaned Features:")
    print(x)

    # 🧠 Model inference
    risk_score = float(model.predict_proba(x)[0, 1])
    prediction = int(model.predict(x)[0])

    verdict = "🚨 ATTACK" if prediction == 1 else "🟢 BENIGN"

    # 🎯 Risk banding (SOC style)
    if risk_score >= 0.90:
        severity = "CRITICAL"
    elif risk_score >= 0.70:
        severity = "HIGH"
    elif risk_score >= 0.40:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    shap_summary = (
        f"UNSW-NB15 XGBoost detected {verdict} traffic "
        f"with {severity} risk (score={risk_score:.4f})"
    )

    return {
        **state,
        "risk_score": risk_score,
        "severity": severity,
        "verdict": verdict,
        "shap_summary": shap_summary
    }
