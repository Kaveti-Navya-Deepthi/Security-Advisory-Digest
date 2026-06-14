from src.database import (
    add_ai_columns,
    get_all_advisories,
    update_ai_summary
)

from src.llm_helper import (
    configure_gemini,
    analyze_cve
)

import sqlite3


API_KEY = "YOUR_GEMINI_API_KEY"

model = configure_gemini(API_KEY)

add_ai_columns()

conn = sqlite3.connect("advisory.db")

cursor = conn.cursor()

cursor.execute("""
SELECT cve_id, description
FROM advisories
LIMIT 3
""")

rows = cursor.fetchall()

for cve_id, description in rows:

    print(f"\nAnalyzing {cve_id}...\n")

    result = analyze_cve(model, description)

    update_ai_summary(cve_id, result)

    print(result[:500])

conn.close()