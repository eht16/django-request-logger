Overview
========

A simple app to configure a common logging setup for Django projects.
This app re-configures Django's logging setup, build (or read from
passed HTTP headers) a unique request-id and add a filter to enrich
log records with information from the request (status code,
path, user, ...) and add the previously created request-id to
the log record.

This is most probably not useful to anyone else, it's quite tailored
to my personal needs and is not very configurable (on purpose).


The RequestIDMiddleware class is based on https://github.com/dabapps/django-log-request-id.


DISCLAIMER
==========

This is not a general purpose app. This is tailored for my own personal use
and should not be used unmodified by others.
However, you may use it to learn or to adjust it to  your needs.
Still, these are not the best practices ever and the code might be buggy.


Installation
============
1. Install:

    pip install git+git://github.com/eht16/django-request-logger#egg=django-request-logger

2. Add middleware "" to MIDDLEWARE_CLASSES (ideally near the top):

    MIDDLEWARE_CLASSES = (
        "...",
        "django_request_logger.middleware.RequestIDMiddleware",
        "...",
    )

3. Configure log file path in settings.py:

    DJANGO_REQUEST_LOGFILE = '/var/log/django/myproject.log'

4. Other settings in settings.py:

    # add the request-id to the response HTTP headers, e.g. for logging with Lighttpd
    # set this to resulting header name which should be added, set to None or unset to disable
    DJANGO_REQUEST_SET_REQUEST_ID_HEADER = 'X-LIGHTTPD-REQUESTID'
    # read an already existing request-id from the request HTTP headers, e.g. set by a webserver
    # set this to given header name which should be added, set to None or unset to disable
    DJANGO_REQUEST_LOG_REQUEST_ID_HEADER = 'HTTP_X_REQUEST_ID'


License
=======

Copyright (c) 2014, Enrico Tröger <enrico(dot)troeger(at)uvena(dot)de>
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    * Neither the name django-wakawaka nor the names of its contributors
      may be used to endorse or promote products derived from this software without
      specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
