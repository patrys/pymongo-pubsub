#! /usr/bin/env python
from setuptools import setup, find_packages

version = __import__('pymongo_pubsub').get_version()

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Database',
]

PACKAGE_DATA = {}

REQUIREMENTS = [
    'pymongo >= 1.5',
]

EXTRAS = {}

setup(name='pymongo-pubsub',
      author='Patryk Zawadzki',
      author_email='patrys@gmail.com',
      description='A publish-subscribe pattern implementation for pymongo',
      version = version,
      packages = find_packages(),
      package_data=PACKAGE_DATA,
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      extras_require=EXTRAS,
      platforms=['any'],
      zip_safe=True)
