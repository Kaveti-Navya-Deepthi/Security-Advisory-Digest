import pandas as pd


def extract_cves(nvd_data):

    records = []

    vulnerabilities = nvd_data.get("vulnerabilities", [])

    for item in vulnerabilities:

        cve = item.get("cve", {})

        cve_id = cve.get("id", "N/A")

        description = "No Description"

        descriptions = cve.get("descriptions", [])

        if descriptions:
            description = descriptions[0].get(
                "value",
                "No Description"
            )

        published = cve.get(
            "published",
            "N/A"
        )

        severity = "N/A"
        score = "N/A"

        metrics = cve.get(
            "metrics",
            {}
        )

        if "cvssMetricV31" in metrics:

            cvss = (
                metrics["cvssMetricV31"][0]
                ["cvssData"]
            )

            severity = cvss.get(
                "baseSeverity",
                "N/A"
            )

            score = cvss.get(
                "baseScore",
                "N/A"
            )

        records.append(
            {
                "cve_id": cve_id,
                "severity": severity,
                "cvss_score": score,
                "published": published,
                "description": description,
            }
        )

    return pd.DataFrame(records)