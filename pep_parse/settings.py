from pathlib import Path

BOT_NAME = 'pep_parse'
SPIDER_NAME = 'pep'
STATUS_KEY = 'status'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
ROBOTSTXT_OBEY = True

FIELDS_NAME = ('Статус', 'Количество')
FILE_NAME = 'status_summary_{time}.csv'
DT_FORMAT = '%Y-%m-%dT%H-%M-%S'

BASE_DIR = Path(__file__).parent.parent

ALLOWED_DOMAINS = 'peps.python.org'
START_URLS = 'https://peps.python.org/'

EXPECTED_STATUS = {
    'Accepted': 0,
    'Active': 0,
    'Deferred': 0,
    'Draft': 0,
    'Final': 0,
    'Provisional': 0,
    'Rejected': 0,
    'Superseded': 0,
    'Withdrawn': 0
}

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
