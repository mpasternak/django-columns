#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import columns

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = columns.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'Django>=1.5.1'
]

test_requirements = [
    'coverage'
]

setup(
    name='django-columns',
    version=version,
    description="""Django template filter for splitting a list into columns.""",
    long_description=readme + '\n\n' + history,
    author='Audrey Roy Greenfeld',
    author_email='audreyr@gmail.com',
    url='https://github.com/audreyr/django-columns',
    packages=[
        'columns',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='django-columns',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=test_requirements
)