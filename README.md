# 🛡️ Agentic Honey-Pot API

> **Automated Cyber-Intelligence Extraction for Modern Scam Detection**
> Detect • Analyze • Extract • Protect

---

## 📖 Project Overview

**Agentic Honey-Pot API** is an AI-powered cyber-intelligence system developed for the **India AI Impact Buildathon**.

The platform automatically detects, classifies, and extracts intelligence from scam messages — including phishing attempts, UPI frauds, and job scams — using advanced LLM reasoning powered by **Gemini 2.5 Flash**.

Instead of just detecting scams, the system extracts actionable cyber intelligence like:

✅ UPI IDs
✅ Malicious links
✅ Phone numbers
✅ Psychological manipulation tactics

This helps security analysts and cybercrime teams accelerate investigation workflows and improve scam reporting automation.

---

## ✨ Key Features

### 🧠 Intelligent Scam Detection

Advanced AI reasoning tailored for Indian scam patterns:

* Electricity bill fraud
* Like & Earn scams
* Fake job offers
* UPI payment fraud

### 📊 Structured Intelligence Extraction

Automatically extracts:

* UPI IDs
* URLs
* Phone numbers
* Threat categories
* Psychological tactics

### ⚡ Rate-Limit Resilience

* Built with **Exponential Backoff** using Tenacity.
* Ensures high reliability during heavy automated evaluation.

### 🔐 Secure API Authentication

* Mandatory API key validation via request headers.
* Production-ready security design.

---

## 🛠️ Tech Stack

| Category      | Technology                           |
| ------------- | ------------------------------------ |
| Language      | Python 3.10+                         |
| Framework     | FastAPI                              |
| AI Engine     | Google Gen AI SDK (Gemini 2.5 Flash) |
| Server        | Uvicorn (ASGI)                       |
| Configuration | Dotenv                               |

---

## 🚀 Quick Start

### 1️⃣ Prerequisites

* Python 3.10 or higher
* Google AI Studio API Key

---

### 2️⃣ Installation

```bash
git clone https://github.com/Priyadharshan-19/Agentic-Honey-Pot-API.git
cd Agentic-Honey-Pot-API
pip install -r requirements.txt
```

---

### 3️⃣ Environment Setup

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_ai_studio_key
SUBMISSION_API_KEY=IndiaAI_Build_2024_Secure
```

---

### 4️⃣ Running the Server (Local)

```bash
python -m uvicorn main:app --reload
```

Local Swagger API Docs:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🌐 Live API Documentation

You can directly test the deployed live API here:

👉 [https://agentic-honey-pot-api-ldb8.onrender.com/docs](https://agentic-honey-pot-api-ldb8.onrender.com/docs)

Upload or send messages through Swagger UI to analyze scam intelligence in real-time.

---

## 📡 API Documentation

### 🔎 Analyze Message

**Endpoint**

```
POST /analyze
```

**Headers**

```
x-api-key: IndiaAI_Build_2024_Secure
```

---

### Request Body

```json
{
  "message": "Your electricity will be cut tonight at 9 PM. Call our officer at 9876543210 to update your bill."
}
```

---

### Response Example

```json
{
  "success": true,
  "intelligence": {
    "category": "Electricity Bill Scam",
    "urgency_level": 9,
    "tactic": "Fear/Authority",
    "entities": {
      "phone_numbers": ["9876543210"]
    }
  }
}
```

---

## ⚖️ Ethical Design & Security

This project follows a **Safety-First Defensive Security Model**.

✅ Designed for cybersecurity research and defensive analysis
✅ No victim PII storage
✅ Transparent reasoning for scam classification
✅ Supports responsible cybercrime reporting workflows

---

## 👨‍💻 Developer

**Priyadharshan M**
2nd Year B.E. (CSE) — SNS College of Technology

> *"Turning AI into a shield against digital fraud."*

