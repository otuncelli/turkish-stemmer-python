#!/usr/bin/env python
import io
import setuptools

with io.open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='TurkishStemmer',
    version='1.3',
    description='Turkish Stemmer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Hanefi Onaldi',
    author_email='abdullahanefi16@gmail.com',
    url='https://github.com/hanefi/turkish-stemmer-python',
    packages=setuptools.find_packages(),
    package_data={'':['*.txt'],},
   )
