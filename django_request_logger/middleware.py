# -*- coding: utf-8 -*-

"""
This module is shamelessly stolen from
https://github.com/dabapps/django-log-request-id
and stripped down to my needs.
"""

from django.conf import settings
from django_request_logger import (
    NO_REQUEST_ID,
    REQUEST_ID_HEADER_SETTING,
    REQUEST_ID_RESPONSE_HEADER_SETTING,
    local)
import uuid


########################################################################
class RequestIDMiddleware(object):

    #----------------------------------------------------------------------
    def process_request(self, request):
        request_id = self._get_request_id(request)
        local.request_id = request_id
        request.id = request_id

    #----------------------------------------------------------------------
    def _get_request_id(self, request):
        request_id_header = getattr(settings, REQUEST_ID_HEADER_SETTING, None)
        if request_id_header:
            return request.META.get(request_id_header, NO_REQUEST_ID)
        return self._generate_id()

    #----------------------------------------------------------------------
    def _generate_id(self):
        return uuid.uuid4().hex

    #----------------------------------------------------------------------
    def process_response(self, request, response):
        header_name = getattr(settings, REQUEST_ID_RESPONSE_HEADER_SETTING, None)
        if header_name and hasattr(local, 'request_id'):
            response[header_name] = local.request_id
        return response
