# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys

import forest

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = forest.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django_forest',
    version=version,
    description='Composite views for REST services.',
    long_description=readme + '\n\n' + history,
    author='Ali Zaidi',
    author_email='alixedi@gmail.com',
    url='https://github.com/alixedi/django_forest',
    packages=[
        'forest',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django_forest',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)