#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="smtproutes",
    version="1.2.9",
    description="A simple, Sinatra inspired, SMTP routing server.",
    author="Benjamin Coe",
    author_email="bencoe@gmail.com",
    url="https://github.com/bcoe/smtproutes",
    packages = find_packages(),
    install_requires = [
        'secure-smtpd>=1.1.8',
        'pydkim',
        'dnspython',
        'pyspf',
        'pydns'
    ],
    tests_require=[
        'nose'
    ]
)