from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Ex Mente Junior Developer Assignment'

setup(
	name='DataAnalysis',
	version=VERSION,
	author='Nicholas Holtzhausen',
	author_email='nholtzhausen54@gmail.com',
	description=DESCRIPTION,
	packages=find_packages,
	install_requires=['pandas', 'matplotlib', 'subprocess'],
	keywords=['python', 'data', 'analysis']
)
