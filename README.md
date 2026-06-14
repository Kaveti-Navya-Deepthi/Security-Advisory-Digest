# AI Security Advisory Digest

## Team Members

1. Kaveti Navya Deepthi
2. Irikireddy Navya Sri
3. Kalabai Gopi Chand
4. Gunjara Keerthana

---

# Project Overview

AI Security Advisory Digest is a cybersecurity project developed to simplify vulnerability analysis. The application collects vulnerability information from the National Vulnerability Database (NVD), processes the data, stores it in a local database, and uses Google Gemini AI to generate security insights.

The main objective of this project is to help users quickly understand the severity, impact, and recommended actions for newly discovered vulnerabilities without manually reading lengthy security advisories.

---

# Problem Statement

New security vulnerabilities are published every day, making it difficult for organizations and security teams to manually analyze every advisory.

Understanding the severity, impact, and mitigation steps of each vulnerability requires significant effort and expertise.

This project automates part of that process by collecting vulnerability information from NVD, organizing it, and generating AI-assisted summaries that make security advisories easier to understand.

---

# Features Implemented

* Fetch vulnerability information from the NVD API
* Process and organize CVE data
* Store advisory records in SQLite
* Generate AI-powered security summaries using Gemini AI
* Interactive Streamlit dashboard
* Vulnerability severity visualization using Plotly
* Risk analysis and mitigation recommendations
* Search and review stored advisories

---

# Architecture Overview

```text
National Vulnerability Database (NVD)
                │
                ▼
         Data Collection
         (fetch_nvd.py)
                │
                ▼
         Data Processing
         (processor.py)
                │
                ▼
          SQLite Database
          (database.py)
                │
                ▼
        Gemini AI Analysis
         (llm_helper.py)
                │
                ▼
        Streamlit Dashboard
             (app.py)
```

## Component Description

### Data Collection

The application retrieves vulnerability information from the NVD API.

### Data Processing

Important fields are extracted:

* CVE ID
* Severity
* CVSS Score
* Published Date
* Description

### Database Layer

Processed vulnerability information is stored in SQLite.

### AI Analysis Layer

Gemini AI generates:

* Vulnerability Summary
* Risk Assessment
* Impact Analysis
* Recommended Actions

### Dashboard Layer

Displays vulnerability information and visual analytics through Streamlit.

---

# Tools and Technologies Used

| Component            | Technology              |
| -------------------- | ----------------------- |
| Programming Language | Python                  |
| Frontend             | Streamlit               |
| Database             | SQLite                  |
| Data Processing      | Pandas                  |
| Visualization        | Plotly                  |
| AI Model             | Google Gemini 2.5 Flash |
| API Source           | NVD API                 |
| Testing              | Pytest                  |

---

# Project Structure

```text
security-advisory-digest/

├── app.py
├── generate_digest.py
├── requirements.txt
├── README.md
├── prompts.md
├── ai_usage_note.md
│
├── data/
│   └── sample_input.json
│
├── outputs/
│   └── security_digest.md
│
├── src/
│   ├── __init__.py
│   ├── fetch_nvd.py
│   ├── processor.py
│   ├── database.py
│   ├── llm_helper.py
│   ├── report_generator.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   └── test_basic.py
│
├── test_database.py
├── test_gemini.py
└── test_processor.py
```

---

# Setup Instructions

## Step 1: Clone the Repository

```bash
git clone <repository-url>
cd security-advisory-digest
```

## Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

## Step 3: Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate.bat
```

## Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

## Step 5: Configure Gemini API Key

Generate a Gemini API key using Google AI Studio and update the API key value in the project configuration before running AI-related features.

---

# Run Instructions

## Start the Dashboard

```bash
streamlit run app.py
```

The application will automatically open in your web browser.

## Fetch Vulnerability Data

1. Open the application.
2. Select **Fetch from NVD** from the sidebar.
3. Choose the number of advisories.
4. Click **Fetch Latest Advisories**.

## Generate AI Analysis

```bash
python generate_digest.py
```

This script reads vulnerability descriptions from the database, sends them to Gemini AI, and stores the generated summaries.

---

# Sample Input

Example vulnerability record:

```json
{
  "cve_id": "CVE-2025-1001",
  "severity": "HIGH",
  "cvss_score": 8.8,
  "description": "Remote code execution vulnerability."
}
```

---

# Sample Output

Example AI-generated analysis:

**Summary:**
Remote code execution vulnerability allowing attackers to execute arbitrary code on the target system.

**Risk Level:**
High

**Impact:**
Attackers may gain unauthorized access and compromise system integrity.

**Recommended Action:**
Apply vendor patches immediately and restrict unnecessary network access.

---

# Running Tests

The project includes a happy-path test case using pytest.

Run:

```bash
pytest tests/test_basic.py
```

Expected Output:

```text
============================= test session starts =============================

collected 1 item

tests/test_basic.py .                                            [100%]

============================== 1 passed ===============================
```

This test verifies that the vulnerability processing module correctly extracts CVE information from valid NVD data and returns the expected output.

---

# AI Capability Demonstrated

The project uses Google Gemini AI to:

* Summarize vulnerability descriptions
* Assess security risks
* Explain potential impact
* Recommend mitigation actions

The AI-generated analysis helps users understand security advisories more quickly and effectively.

---

# Assumptions

The project assumes:

1. Internet connectivity is available.
2. The NVD API is accessible.
3. A valid Gemini API key is configured.
4. Vulnerability data is returned in the expected format.
5. SQLite is sufficient for project-scale storage.

---

# Limitations

1. The application depends on the availability of the NVD API.
2. AI-generated summaries may occasionally contain inaccuracies.
3. SQLite is suitable for small to medium datasets only.
4. The project currently supports only NVD vulnerability data.
5. Real-time alerting functionality is not implemented.
6. AI recommendations should not replace professional security analysis.

---

# Future Scope

* PDF report generation
* Automated email notifications
* Real-time vulnerability monitoring
* Integration with additional threat intelligence sources
* Advanced analytics and trend analysis
* Cloud deployment
* User authentication and authorization

---

# Demo Video

Video Link:

link--> https://drive.google.com/file/d/19twPyIl4u3nMmB6We4dCanHOez0Hh_b3/view?usp=drive_link

Replace the above link with the final YouTube or Google Drive demo video before submission.

---

# Conclusion

AI Security Advisory Digest was developed to simplify vulnerability analysis by combining cybersecurity data with artificial intelligence. The project demonstrates how vulnerability intelligence, data processing, database management, AI analysis, and dashboard visualization can work together to provide meaningful security insights in an easy-to-use application.
