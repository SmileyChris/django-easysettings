#!/usr/bin/env python
from distutils.core import setup

try:
    import easysettings
    long_description = easysettings.__doc__
except ImportError:
    long_description = ''

setup(
    name='django-easysettings',
    version='1.0',
    url='http://github.com/SmileyChris/django-easysettings',
    description='Easy app-specific settings for Django',
    long_description=long_description,
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
