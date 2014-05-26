# coding: utf-8

from django.conf import settings
from django_request_logger import DJANGO_REQUEST_LOGFILE_SETTING


# it is dirty to configure logging this way in real code instead of a config file
# but in this case on purpose to have one logging config easily pluggable
# into multiple projects
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'WARN',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'logstash': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': getattr(settings, DJANGO_REQUEST_LOGFILE_SETTING),
            'mode': 'a',
            'filters': ['process_request'],
            'formatter': 'logstash'
        },
    },
    'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse'
         },
         'process_request': {
             '()': 'django_request_logger.filters.ProcessRequest'
         }
     },
    'formatters': {
        'logstash': {
            'format': '%(asctime)s [%(process)d] [%(levelname)s] [%(threadName)s] [%(name)s|%(module)s] [%(request_id)s] [%(site)s] [%(remote_address)s] [%(status_code)s] [%(user)s] [%(absolute_url)s]: %(message)s'
        },
    },
    'loggers': {
        '': {
            'handlers': ['mail_admins', 'logstash'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['mail_admins', 'logstash'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db': {
            'handlers': ['mail_admins', 'logstash'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'logstash'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
