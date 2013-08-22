"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

APP = ['test.py']
DATA_FILES = ['resources']
OPTIONS = {'argv_emulation': False}

setup(
      app=APP,
      data_files=DATA_FILES,
      options={'py2app': OPTIONS},
      setup_requires=['py2app'],
      )
