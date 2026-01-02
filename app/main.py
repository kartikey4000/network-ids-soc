from graph.workflow import graph

initial_state = {
   "alert": {
        "dur": 180.5,

        "sbytes": 9500000,
        "dbytes": 8200000,

        "Spkts": 45000,
        "Dpkts": 38000,

        "smeansz": 1200,
        "dmeansz": 1050,

        "Sload": 8.5e6,
        "Dload": 7.9e6,

        "tcprtt": 0.45,
        "synack": 0.22,
        "ackdat": 0.35,

        "Sintpkt": 0.0001,
        "Dintpkt": 0.00015,

        "Sjit": 0.85,
        "Djit": 0.78,

        "swin": 1024,
        "dwin": 2048,

        "ct_state_ttl": 12,
        "ct_flw_http_mthd": 0,
        "is_ftp_login": 0,
        "ct_ftp_cmd": 0,

        "ct_srv_src": 95,
        "ct_srv_dst": 110,
        "ct_dst_ltm": 60,
        "ct_src_ ltm": 70,
        "ct_src_dport_ltm": 55,
        "ct_dst_sport_ltm": 65,
        "ct_dst_src_ltm": 120,

        "is_sm_ips_ports": 1
    }
,

    "risk_score": 0.0,
    "shap_summary": None,
    "investigation_notes": None,
    "decision": None,
    "report": None
}

result = graph.invoke(initial_state)
print(result)
