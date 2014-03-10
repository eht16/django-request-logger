# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

NAME = 'django-request-logger'

VERSION = '0.1'

DESCRIPTION = """\
A specific Django logging configuration to send log messages
in a specific format to a log file so that the messages
can be forwarded to and easily parsed Logstash.
"""

setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    version=VERSION,
    author='Enrico Tröger',
    author_email='enrico.troeger@uvena.de',
    url='https://github.com/eht16/django-request-logger',
    packages=find_packages(),
    license = "BSD",
    include_package_data=True,
    zip_safe=False,
    requires=['django'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
