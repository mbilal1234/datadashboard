# import the datadog API (e.g., initialize, api)
from datadog import initialize, api
from pathlib import Path

import os

DATADOG_APPLICATION_KEY = os.getenv("DATADOG_APPLICATION_KEY")
DATADOG_API_KEY = os.getenv("DATADOG_API_KEY")

JSON_FILES = [  # TODO: list out the files
    "cobalt-analytics.json",
    "cobalt-monitoring.json",
]

def main():
    # TODO: initialize datadog API

    for dashboard_file in JSON_FILES:
        if has_file_changed(dashboard_file):
            upload_dashboard_to_datadog(dashboard_file)

def has_file_changed(dashboard_file):
    # TODO: Implement this method
    # return True if changed, or False if not changed
    return True

def upload_dashboard_to_datadog(dashboard_file):
    dashboard_json = Path(dashboard_file).read_text()
    # TODO: use api to upload dashboard
    # TODO: use application key, use api key

if __name__ == "__main__":
    main()
