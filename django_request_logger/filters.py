# coding: utf-8

import logging
from django.contrib.sites.models import RequestSite
from django_request_logger import local, NO_REQUEST_ID


########################################################################
class ProcessRequest(logging.Filter):

    #----------------------------------------------------------------------
    def _get_site_domain(self, request):
        # delay import as this module is imported too early by the logging config
        site = RequestSite(request)
        return site.domain

    #----------------------------------------------------------------------
    def filter(self, record):
        record.request_id = getattr(local, 'request_id', NO_REQUEST_ID)

        if hasattr(record, 'request'):
            request = record.request
            client_ip = request.META.get('REMOTE_ADDR')
            if 'HTTP_X_FORWARDED_FOR' in request.META and client_ip != request.META['HTTP_X_FORWARDED_FOR']:
                client_ip += ' (%s)' % request.META['HTTP_X_FORWARDED_FOR']
            record.remote_address = client_ip
            record.absolute_url = request.build_absolute_uri()
            record.user = request.user

            site_domain = self._get_site_domain(request)
            record.site = site_domain
        else:
            record.remote_address = '-'
            record.absolute_url = '-'
            record.user = '-'
            record.status_code = '-'
            record.site = '-'
        return super(ProcessRequest, self).filter(record)
