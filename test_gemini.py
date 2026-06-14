from src.llm_helper import configure_gemini, analyze_cve

API_KEY = "YOUR_GEMINI_API_KEY"

model = configure_gemini(API_KEY)

description = """
Remote code execution vulnerability allowing attackers
to execute arbitrary code on the target system.
"""

result = analyze_cve(model, description)

print(result)