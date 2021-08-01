# import the datadog API (e.g., initialize, api)
from datadog import initialize, api
from pathlib import Path
import json
import sys
import os


DATADOG_APPLICATION_KEY = os.getenv("DATADOG_APPLICATION_KEY")
DATADOG_API_KEY = os.getenv("DATADOG_API_KEY")

JSON_FILES = [  # TODO: list out the files
    "cobalt-analytics.json",
    "cobalt-monitoring.json",
]

def main():
    # TODO: initialize datadog API
    options = {
        'api_key': DATADOG_API_KEY,
        'app_key': DATADOG_APPLICATION_KEY
    }

    initialize(**options)

    for dashboard_file in JSON_FILES:
        if has_file_changed(dashboard_file):
            upload_dashboard_to_datadog(dashboard_file)

def has_file_changed(dashboard_file):
    # TODO: Implement this method
    # return True if changed, or False if not changed
    return True



def update_dash(dash_dict, board_type):
    if board_type == "timeboard":
        title = dash_dict.get('title', 'New Timeboard')
        read_only = dash_dict.get('read_only', 'False')
        description = dash_dict.get('description', '')
        graphs = dash_dict.get('graphs', [])
        template_variables = dash_dict.get('template_variables', [])
        res = api.Timeboard.update(title=title, description=description, graphs=graphs,
                                   template_variables=template_variables, read_only=read_only)
        if res.get('errors', None):
            print(res)
        else:
            print("Successfully created timeboard")
    elif board_type == "screenboard":
        title = dash_dict.get('board_title', 'New Screenboard')
        description = dash_dict.get('description', '')
        widgets = dash_dict.get('widgets', [])
        width = dash_dict.get('width', 1024)
        template_variables = dash_dict.get('template_variables', [])
        res = api.Screenboard.update(board_title=title, description=description,
                                     widgets=widgets, template_variables=template_variables, width=width)
        if res.get('errors', None):
            print(res)
        else:
            print("Successfully created screenboard")
    else:
        print_error("Board type undefined")
        
def print_error(msg):
    print("\nERROR: {}\n".format(msg))
    sys.exit(1)       
        
def upload_dashboard_to_datadog(dashboard_file):
    dashboard_json = Path(dashboard_file).read_text()
    # TODO: use api to upload dashboard
    # TODO: use application key, use api key
    if not dashboard_json:
        print_error("Must specify a json file when creating a dashboard")
    try:
        with open(dashboard_json) as data_file:
            data = json.load(data_file)
        board_type = ''
        if data.get('widgets', None):
            board_type = "screenboard"
        elif data.get('graphs', None):
            board_type = "timeboard"
        if data and board_type:
            update_dash(data, board_type)
        else:
            print_error("Could not load data from JSON file")
    except:
        print_error("There was an error updating the dashboard")

if __name__ == "__main__":
    main()

