#!/usr/bin/python2.7
from setuptools import setup
from subprocess import call

setup(name='Safari Crash',
      version='1.0',
      description='''Safari Crash is an exploit toolkit for quick deployment of 
      Safari and other HTML exploits aimed at mobile browsers''',
      author='TheSecondSun',
      author_email='thescndsun@gmail.com'
     )

call("pip install -r requirements.txt", shell=True)
