#!/bin/python3
# coding: utf-8
"""mlogtest setup file."""

# To use a consistent encoding
from codecs import open
from os import path

from setuptools import find_packages, setup

from mlogtest import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mlogtest',
    version=__version__,
    description='A project for preparing MongoDB logs for automated testing',
    long_description=long_description,
    url='https://github.com/kallimachos/mlogtest',
    author='Brian moss',
    author_email='kallimachos@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Database',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='MongoDB database logs',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'mlogtest=mlogtest:main',
            'difflogs=difflogs:main',
        ],
    },
)
