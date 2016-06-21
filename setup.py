#!/usr/bin/env python

try:
  from setuptools import setup
except ImportError:
  from disutils.core import setup

__version__ = '0.1.0-alpha'

setup(
    name          = 'CLIMerriamWebster'
    version       = __version__,
    description   = 'A Linux command line tool to look up definitions and synonyms for words using the Merriam Webster, Dicionary.com resource.',
    author        = 'Seth Cook',
    author_email  = 'sethcook@purdue.edu',
    classifiers   = [ 
        'Programming Language :: Python :: 2 :: Only',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    packages      = [ 'climw' ],
    entry_points  = {
        'console_scripts': [
            'mw = climw.__main__:main',
        ],
    },
)
