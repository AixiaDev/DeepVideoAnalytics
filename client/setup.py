#!/usr/bin/env python

from distutils.core import setup

setup(name='DeepVideoAnalyticsClient',
      version='1.0',
      description='Deep Video Analytics Client',
      author='Akshay Bhat',
      author_email='dvaclient@deepvideoanalytics.com',
      url='https://www.deepvideoanalytics.com/',
      packages=['dvaclient'],
      package_data={'dvaclient': ['schema.json']},
      include_package_data=True,
      install_requires=[
            'jsonschema',
            'requests'
      ],
      )
