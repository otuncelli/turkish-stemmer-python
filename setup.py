#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='TurkishStemmer',
    version='1.1',
    description='Turkish Stemmer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Hanefi Önaldı',
    author_email='abdullahanefi16@gmail.com',
    url='https://github.com/hanefi/turkish-stemmer-python',
    packages=setuptools.find_packages(),
   )
