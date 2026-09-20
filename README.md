# TRACE-X

### Forensic-Grade, AI-Assisted Multi-Source Cyber Fraud Investigation & Evidence Correlation Platform

TRACE-X is a prototype investigation platform designed to help investigators correlate information from multiple cyber-fraud data sources, build an evidence-backed investigation graph, identify suspicious patterns, and maintain traceability between findings and their underlying records.

The project focuses on making relationships between entities such as **phone numbers, IMEI/device identifiers, IP addresses, UPI IDs, and bank accounts** easier to investigate and understand.

---

## 🎯 Problem

Cyber-fraud investigations often involve information scattered across different sources such as:

* Telecom records
* Device information
* IP/session records
* UPI and financial transactions
* Account/KYC information

The challenge is to connect these records without creating unsupported or false relationships.

TRACE-X aims to provide a structured way to:

1. Ingest and normalize investigation data
2. Resolve entities across different data sources
3. Build an evidence-backed relationship graph
4. Identify suspicious transaction and entity patterns
5. Provide traceable evidence for every important relationship
6. Present the investigation through an investigator-friendly interface

---

## 🚀 Key Features

### 1. Multi-Source Data Correlation

TRACE-X works with multiple investigation data sources and connects related entities.

Example:

```text
Phone Number
     │
     ▼
   IMEI
     │
     ▼
   UPI ID
     │
     ▼
Bank Account
```

---

### 2. Investigation Graph

Relationships are represented as a graph where:

* **Nodes** represent entities
* **Edges** represent relationships
* **Evidence references** explain where each relationship originated

Example:

```text
VICTIM_001
     │
     │ ₹50,000
     ▼
  UPI_001
     │
     │ ₹48,000
     ▼
  UPI_002
     │
     │ ₹45,000
     ▼
  UPI_003
```

---

### 3. Evidence Traceability

TRACE-X retains evidence references alongside relationships.

Example:

```json
{
  "source": "UPI_001",
  "target": "UPI_002",
  "type": "TRANSFERRED",
  "amount": 48000,
  "timestamp": "2026-09-19 10:12:00",
  "evidence": "transactions.csv:2"
}
```

This allows investigators to trace a graph relationship back to the underlying record.

---

### 4. Timeline Analysis

Investigation events can be organized chronologically to help identify sequences such as:

```text
10:10 → Victim transfers money
10:12 → UPI_001 transfers money onward
10:15 → UPI_002 transfers money onward
10:20 → UPI_003 transfers money onward
```

---

### 5. Anomaly & Risk Indicators

TRACE-X uses explainable indicators to identify potentially suspicious patterns, such as:

* Rapid onward transfers
* High transaction velocity
* Shared device identifiers
* Repeated beneficiaries

The system is designed to provide **evidence-backed indicators**, rather than making unsupported conclusions.

---

### 6. Investigation Reports

The project includes a reporting layer intended to convert investigation findings into a human-readable report containing relevant entities, relationships, timelines, alerts, and evidence references.

---

## 🏗️ Project Structure

```text
TRACE-X/
│
├── data/
│   └── sample_relationships.json
│
├── src/
│   ├── graph.py
│   ├── timeline.py
│   ├── anomaly.py
│   └── risk.py
│
├── output/
│   ├── graph.json
│   ├── timeline.json
│   ├── alerts.json
│   └── risk.json
│
├── dashboard/
│   └── dashboard.py
│
├── tests/
│   ├── test_graph.py
│   ├── test_timeline.py
│   ├── test_anomaly.py
│   └── test_risk.py
│
├── reports/
│
└── README.md
```

---

## 🔄 System Architecture

```text
             ┌─────────────────────┐
             │   Investigation     │
             │       Data          │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Ingestion &         │
             │ Normalization       │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Entity Resolution   │
             │ & Correlation       │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Investigation Graph │
             └──────────┬──────────┘
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
        Timeline    Anomaly     Risk
        Analysis    Detection   Indicators
             │          │          │
             └──────────┼──────────┘
                        ▼
             ┌─────────────────────┐
             │ Investigator       │
             │ Dashboard          │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Investigation      │
             │ Report             │
             └─────────────────────┘
```

---

## 🧰 Technology Stack

### Backend / Analytics

* Python
* NetworkX
* JSON-based data exchange

### Frontend

* Streamlit
* Interactive investigation visualizations

### Analysis

* Graph-based entity correlation
* Rule-based anomaly detection
* Risk indicators
* Timeline analysis

### Testing

* Pytest

---

## 📊 Example Investigation

The current prototype includes mock relationships representing a potential transaction chain:

```text
VICTIM_001
    │
    ▼
UPI_001
    │
    ▼
UPI_002
    │
    ▼
UPI_003
    │
    ▼
BANK_001
```

A shared device relationship is also represented:

```text
PHONE_001 ─────┐
               ▼
            IMEI_001
               ▲
               │
PHONE_002 ─────┘
```

These relationships can be analyzed together to provide investigators with a connected view of the supplied records.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd TRACE-X
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install networkx pytest
```

Additional dependencies will be added as the dashboard and reporting components are implemented.

---

## ▶️ Running the Graph Module

From the project root:

```bash
python src/graph.py
```

The module reads:

```text
data/sample_relationships.json
```

and generates:

```text
output/graph.json
```

---

## 🧪 Running Tests

Run the test suite with:

```bash
python -m pytest
```

---

## 🔐 Evidence & Integrity

TRACE-X is designed around the principle that investigation findings should be traceable to their underlying evidence.

Relationships should retain information such as:

* Source entity
* Target entity
* Relationship type
* Timestamp
* Transaction amount, where applicable
* Evidence/source reference

Future components can extend this with cryptographic integrity mechanisms such as SHA-256 hashes and evidence manifests.

---

## 🤖 AI-Assisted Analysis

AI functionality is intended to assist investigators by summarizing already-established evidence and relationships.

F
