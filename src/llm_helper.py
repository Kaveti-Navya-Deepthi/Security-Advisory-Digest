import google.generativeai as genai


def configure_gemini(api_key):
    genai.configure(api_key=api_key)

    return genai.GenerativeModel("gemini-2.5-flash")


def analyze_cve(model, description):
    prompt = f"""
You are a cybersecurity analyst.

Analyze the vulnerability below.

Description:
{description}

Provide:
1. Summary
2. Risk Level
3. Impact
4. Recommended Action
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"ERROR: {e}"