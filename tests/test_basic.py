
from src.processor import extract_cves


def test_extract_cves_happy_path():

    sample_data = {
        "vulnerabilities": [
            {
                "cve": {
                    "id": "CVE-2025-1001",
                    "published": "2025-01-01",
                    "descriptions": [
                        {
                            "lang": "en",
                            "value": "Remote code execution vulnerability."
                        }
                    ],
                    "metrics": {
                        "cvssMetricV31": [
                            {
                                "cvssData": {
                                    "baseSeverity": "HIGH",
                                    "baseScore": 8.8
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }

    df = extract_cves(sample_data)

    assert len(df) == 1
    assert df.iloc[0]["cve_id"] == "CVE-2025-1001"
    assert df.iloc[0]["severity"] == "HIGH"
    assert df.iloc[0]["cvss_score"] == 8.8
