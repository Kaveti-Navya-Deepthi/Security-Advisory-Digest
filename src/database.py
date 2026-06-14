import sqlite3
import pandas as pd

DB_NAME = "advisory.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS advisories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cve_id TEXT,
            severity TEXT,
            cvss_score REAL,
            published TEXT,
            description TEXT,
            ai_summary TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_advisories(df):
    conn = sqlite3.connect(DB_NAME)

    df.to_sql(
        "advisories",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()


def get_all_advisories():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            cve_id,
            severity,
            cvss_score,
            published,
            description,
            ai_summary
        FROM advisories
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def add_ai_columns():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    try:
        cursor.execute(
            "ALTER TABLE advisories ADD COLUMN ai_summary TEXT"
        )
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()


def update_ai_summary(cve_id, summary):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE advisories
        SET ai_summary = ?
        WHERE cve_id = ?
        """,
        (summary, cve_id)
    )

    conn.commit()
    conn.close()


def get_advisories_for_ai(limit=5):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT cve_id, description
        FROM advisories
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows