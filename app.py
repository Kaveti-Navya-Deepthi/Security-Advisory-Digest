
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Project Imports
from src.fetch_nvd import fetch_latest_cves
from src.processor import extract_cves
from src.database import create_database, insert_advisories

# =====================================
# PAGE CONFIGURATION
# =====================================
st.set_page_config(
    page_title="AI Security Advisory Digest",
    page_icon="🛡️",
    layout="wide"
)

# =====================================
# SIDEBAR
# =====================================
st.sidebar.title("⚙️ Controls")

input_source = st.sidebar.radio(
    "Select Input Source",
    [
        "Database",
        "Fetch from NVD",
        "Upload File"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    AI Security Advisory Digest

    Features:
    • NVD Integration
    • Gemini AI Analysis
    • SQLite Storage
    • Dashboard Analytics
    """
)

# =====================================
# HEADER
# =====================================
st.title("🛡️ AI Security Advisory Digest")

st.write(
    "Analyze security advisories, generate AI summaries, and monitor vulnerability trends."
)

# =====================================
# FETCH FROM NVD
# =====================================
if input_source == "Fetch from NVD":

    st.header("🌐 Fetch Latest Advisories")

    count = st.slider(
        "Number of CVEs",
        min_value=5,
        max_value=50,
        value=10
    )

    if st.button("Fetch Latest Advisories"):

        try:

            with st.spinner("Fetching latest advisories from NVD..."):

                create_database()

                data = fetch_latest_cves(count)

                df = extract_cves(data)

                insert_advisories(df)

            st.success(
                f"{len(df)} advisories fetched successfully."
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        except Exception as e:

            st.error(
                f"Fetch Failed: {e}"
            )

# =====================================
# FILE UPLOAD
# =====================================
elif input_source == "Upload File":

    st.header("📂 Upload Advisory File")

    uploaded_file = st.file_uploader(
        "Upload CSV or JSON",
        type=["csv", "json"]
    )

    if uploaded_file is not None:

        st.success(
            f"Uploaded Successfully: {uploaded_file.name}"
        )

        try:

            if uploaded_file.name.endswith(".csv"):

                uploaded_df = pd.read_csv(uploaded_file)

            else:

                uploaded_df = pd.read_json(uploaded_file)

            st.subheader("Uploaded Data")

            st.dataframe(
                uploaded_df,
                use_container_width=True
            )

        except Exception as e:

            st.error(
                f"File Processing Error: {e}"
            )

# =====================================
# DATABASE DASHBOARD
# =====================================
else:

    try:

        conn = sqlite3.connect("advisory.db")

        df = pd.read_sql_query(
            """
            SELECT *
            FROM advisories
            """,
            conn
        )

        # -------------------------
        # Metrics
        # -------------------------
        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Total Advisories",
                len(df)
            )

        with col2:

            high_count = len(
                df[
                    df["severity"]
                    .astype(str)
                    .str.upper()
                    .isin(["HIGH", "CRITICAL"])
                ]
            )

            st.metric(
                "High / Critical",
                high_count
            )

        # -------------------------
        # Advisory Table
        # -------------------------
        st.subheader("📋 Stored Advisories")

        st.dataframe(
            df,
            use_container_width=True
        )

        # -------------------------
        # Severity Chart
        # -------------------------
        st.subheader("📊 Severity Distribution")

        severity_counts = (
            df["severity"]
            .fillna("Unknown")
            .value_counts()
            .reset_index()
        )

        severity_counts.columns = [
            "Severity",
            "Count"
        ]

        fig = px.pie(
            severity_counts,
            names="Severity",
            values="Count",
            title="Vulnerability Severity Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # -------------------------
        # AI Summaries
        # -------------------------
        st.subheader("🤖 AI Generated Summaries")

        if "ai_summary" in df.columns:

            for _, row in df.head(5).iterrows():

                with st.expander(
                    f"{row['cve_id']}"
                ):

                    summary = row.get(
                        "ai_summary",
                        None
                    )

                    if (
                        pd.notna(summary)
                        and str(summary).strip()
                    ):

                        st.write(summary)

                    else:

                        st.warning(
                            "No AI Summary Available"
                        )

        else:

            st.info(
                "AI summaries have not been generated yet."
            )

    except Exception as e:

        st.error(
            f"Database Error: {e}"
        )

    finally:

        try:
            conn.close()
        except:
            pass
