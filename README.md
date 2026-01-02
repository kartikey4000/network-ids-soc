# 🛡️ LLM-Powered SOC Analyst Agent with ML-Based Threat Detection

## 📌 Overview

This project implements a **Security Operations Center (SOC) Analyst Agent** that combines:

* **Machine Learning–based threat detection (XGBoost)**
* **LLM-driven reasoning using LangGraph / LangChain**
* **Automated investigation-style decision support**

The system is designed to **simulate a real SOC workflow**, where raw network or log-derived features are scored by an ML model and then interpreted by an LLM agent to produce human-readable security insights.

---

## 🧠 Architecture (High Level)

```
[ Input Features / Logs ]
            │
            ▼
[ ML Threat Detection Model (XGBoost) ]
            │  (Anomaly / Threat Score)
            ▼
[ SOC Analyst Agent (LangGraph + LLM) ]
            │
            ▼
[ Investigation Summary / Decision Output ]
```

---

## 🤖 Machine Learning Model

* **Algorithm:** XGBoost
* **Purpose:** Network intrusion / anomaly detection
* **Training:** Performed offline using network-flow–level features
* **Model Artifact:** Serialized as `.pkl` / `.joblib`

### ⚠️ Important (Model Files)

The trained ML model **is NOT committed to the repository**.

Reasons:

* Binary files exceed GitHub size limits
* Model artifacts are environment- and version-sensitive
* This follows real-world MLOps best practices

### ✅ How the model is handled

* Model is distributed separately (e.g., GitHub Releases or secure storage)
* At runtime, the SOC agent loads the model from the `agents/` directory

Expected location:

```
agents/
 └── xgboost_model.pkl
```

---

## 📊 Model Training (Kaggle)

The ML model used in this project was trained and evaluated in a Kaggle notebook.

The notebook covers:
- Dataset exploration and preprocessing
- Feature engineering
- Class imbalance handling
- XGBoost training and evaluation
- Model serialization for inference use

🔗 Kaggle Notebook:
https://www.kaggle.com/code/kartikeyahuja/soc-training

## 🧩 SOC Agent

The SOC agent is built using **LangGraph**, enabling:

* Structured investigation flows
* Clear separation between ML inference and reasoning
* Deterministic decision paths

The agent:

1. Loads the trained ML model
2. Scores incoming feature vectors
3. Interprets results using an LLM
4. Produces SOC-style explanations (e.g., suspicious activity, severity, rationale)

---

## 📦 Dependency Management

### ❌ What is NOT included

* `soc-env/` (virtual environment)
* `.pkl`, `.joblib` model files
* Large datasets (`.csv`)

These are intentionally excluded via `.gitignore`.

### ✅ What IS included

* Exact dependency versions in `requirements.txt`

This guarantees reproducibility without committing OS-specific binaries.

---

## 📄 requirements.txt (Exact Versions)

The dependencies are **locked to the exact versions used during model training and inference**, including:

* `xgboost==3.1.2`
* `numpy==1.26.4`
* `scikit-learn==1.3.2`

This avoids serialization and ABI incompatibility when loading the trained model.

---

## 🚀 Setup & Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/kartikey4000/network-ids-soc.git
cd network-ids-soc
```

### 2️⃣ Create virtual environment

```bash
python -m venv soc-env
```

Activate:

* **Windows**

```powershell
soc-env\Scripts\activate
```

* **Linux / macOS**

```bash
source soc-env/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Place trained model

```text
agents/xgboost_model.pkl
```

### 5️⃣ Run the SOC agent

```bash
python main.py
```

---

## 🧪 Reproducibility Philosophy

This project follows **production-grade ML engineering practices**:

* No virtual environments committed
* No binary ML artifacts committed
* Exact dependency pinning
* Clear separation of training vs inference

> "The repository contains only reproducible source code; model artifacts are managed separately."

---

## 🎯 Learning Outcomes

* Practical SOC-style threat detection
* ML + LLM hybrid system design
* LangGraph agent orchestration
* Real-world MLOps hygiene

---

## 📌 Disclaimer

This project is for **educational and research purposes only**. It is not intended for direct deployment in production SOC environments without additional hardening, validation, and security controls.
