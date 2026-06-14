from src.fetch_nvd import fetch_latest_cves
from src.processor import extract_cves
from src.database import (
    create_database,
    insert_advisories,
    get_all_advisories
)

create_database()

data = fetch_latest_cves(10)

df = extract_cves(data)

insert_advisories(df)

rows = get_all_advisories()

print(f"Total Rows in DB: {len(rows)}")

for row in rows[:5]:
    print(row)