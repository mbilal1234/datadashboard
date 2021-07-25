export_dash_sh :-
#!/bin/sh
dash_id='dashboard_id'
api_key='api_key'
app_key='application_key'

curl -X GET "https://app.datadoghq.com/api/v1/dash/${dash_id}?api_key=${api_key}&application_key=${app_key}" | jq '.dash' > dash.json
