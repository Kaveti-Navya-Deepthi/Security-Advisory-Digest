import requests
from datetime import datetime, timedelta


def fetch_latest_cves(results_per_page=20):

    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=30)

    params = {
        "resultsPerPage": results_per_page,
        "pubStartDate": start_date.strftime("%Y-%m-%dT00:00:00.000"),
        "pubEndDate": end_date.strftime("%Y-%m-%dT23:59:59.999")
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":

    data = fetch_latest_cves(10)

    print(
        f"Total CVEs fetched: {len(data['vulnerabilities'])}"
    )

    for cve in data["vulnerabilities"][:5]:

        print(
            cve["cve"]["id"]
        )