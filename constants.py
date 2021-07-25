"""
Module containing constants
""""
DATADOG_BASE_URL = 'https://app.datadoghq.com'
DATADOG_SETTINGS_URL = '{}/account/settings#api'.format(DATADOG_BASE_URL)

## help texts
CLI_DESC = ('Module that enables user to create a Datadog Timeboard based on'
             'the JSON template input')
CLI_APP_KEY_HELP = ('Datadog Application Key. To find or create it, please '
                    'visit {}').format(DATADOG_SETTINGS_URL)
CLI_API_KEY_HELP = ('Datadog API Key. To find or create it, please visit {}'
                    .format(DATADOG_SETTINGS_URL))
CLI_DESCRIPTION_HELP = 'A description for your dashboard'
CLI_READ_ONLY_HELP = 'If specified, the dashboard will be read-only'
CLI_REPLICA_DB_HELP = 'The read replica db instance identifier'
CLI_SOURCE_DB_HELP = 'The primary/source db instance identifier'
CLI_TEMPLATE_FILE_HELP = ('The name of the file containing your dashboard '
                          'template. By default input is taken from the '
                          'terminal and is terminated by an EOF')
CLI_TITLE_HELP = 'The title of your dashboard'

## default argument values
DEFAULT_DESCRIPTION = ('RDS PostgreSQL Instance Replication Timeboard that'
                       'displays different metrics associated with a source db'
                       'instance and a read replica instance')
DEFAULT_READ_ONLY = False
DEFAULT_TITLE = 'My RDS PostgreSQL Instance Replication Monitor'
DEFAULT_ARG_VALUES = {
  'description': DEFAULT_DESCRIPTION,
  'read_only': DEFAULT_READ_ONLY,
  'title': DEFAULT_TITLE
}
