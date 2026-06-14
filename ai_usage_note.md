# AI Usage Note

## AI Model Used

Google Gemini 2.5 Flash

---

## Purpose of AI in This Project

AI was used to analyze vulnerability descriptions obtained from the National Vulnerability Database (NVD).

The model helps convert technical vulnerability information into easy-to-understand security insights by generating:

* Vulnerability summaries
* Risk assessments
* Impact explanations
* Recommended mitigation actions

The goal was to reduce the time required to manually analyze vulnerability advisories.

---

## What AI Helped With

The Gemini model assisted in:

### 1. Vulnerability Summarization

Converting long technical vulnerability descriptions into concise summaries.

### 2. Risk Assessment

Identifying the likely severity and security impact of a vulnerability.

### 3. Impact Analysis

Explaining how a vulnerability could affect systems, applications, or users.

### 4. Mitigation Recommendations

Suggesting security measures such as patching, configuration changes, or monitoring activities.

### 5. Improving Readability

Transforming technical security information into a format that is easier for users to understand.

---

## What AI Got Wrong or Required Human Review

During testing, some limitations were observed:

### 1. Overly Generic Recommendations

The model occasionally suggested broad recommendations such as:

* "Apply security patches"
* "Monitor system logs"

without providing product-specific guidance.

### 2. Assumed Missing Context

When vulnerability descriptions lacked technical details, the model sometimes made assumptions about the affected systems.

### 3. Inconsistent Risk Ratings

In some cases, the AI-generated risk assessment did not fully match the official CVSS severity published by NVD.

### 4. Repetitive Responses

Multiple vulnerabilities with similar descriptions occasionally produced similar summaries and recommendations.

### 5. Not a Replacement for Expert Review

AI-generated outputs should be considered supporting information and not a substitute for official vendor advisories or professional security analysis.

---

## Human Validation Process

To improve reliability:

1. Vulnerability data was obtained directly from NVD.
2. AI outputs were reviewed manually.
3. Official severity information was retained alongside AI-generated insights.
4. AI recommendations were treated as guidance rather than authoritative security decisions.

---

## Best Prompts Used

### Prompt Version 1

```text
You are a cybersecurity analyst.

Analyze the vulnerability below.

Description:
{description}

Provide:
1. Summary
2. Risk Level
3. Impact
4. Recommended Action
```

This prompt produced the most balanced and readable results.

---

### Prompt Version 2

```text
You are a senior cybersecurity analyst.

Analyze the following CVE description and provide:

- Executive Summary
- Risk Assessment
- Potential Impact
- Mitigation Recommendations

Description:
{description}
```

This version generated more detailed explanations but occasionally produced longer responses than required.

---

### Prompt Version 3

```text
Explain this vulnerability to an IT administrator.

Description:
{description}

Include:
- What the vulnerability does
- Why it is dangerous
- Recommended next steps
```

This prompt produced simpler explanations suitable for non-security users.

---

## Final Prompt Used in the Project

```text
You are a cybersecurity analyst.

Analyze the vulnerability below.

Description:
{description}

Provide:
1. Summary
2. Risk Level
3. Impact
4. Recommended Action
```

This prompt was selected because it produced consistent, concise, and actionable results across different vulnerability descriptions.

---

## Conclusion

AI was used as an assistance tool to improve the speed and readability of vulnerability analysis. While it helped generate summaries and recommendations, human review remains important to ensure accuracy and alignment with official security guidance.
