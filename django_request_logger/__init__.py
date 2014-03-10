# -*- coding: utf-8 -*-

from django.conf import settings, LazySettings
from django_request_logger.log import LOGGING
import threading

__version__ = "0.1"

# ThreadLocal - dirty but does the job
local = threading.local()


REQUEST_ID_HEADER_SETTING = 'LOG_REQUEST_ID_HEADER'
NO_REQUEST_ID = '-'

# override any existing logging configuration
settings.LOGGING = LOGGING

# create a new Settings object and pass in our settings,
# we don't need/use the new Settings object, it is just to
# get the private _configure_logging() method called
unused_settings = LazySettings()
unused_settings.configure(default_settings=settings)
