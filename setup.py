#!/usr/bin/env python
from setuptools import setup

setup(
    name='django-easysettings',
    version='1.1',
    url='http://github.com/SmileyChris/django-easysettings',
    description='Easy app-specific settings for Django',
    long_description=open('README.rst', 'r').read(),
    author='Chris Beaven',
    author_email='smileychris@gmail.com',
    platforms=['any'],
    py_modules=['easysettings'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
