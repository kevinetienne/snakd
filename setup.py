#!/usr/bin/env python

from distutils.core import setup

version = "0.0.1"

setup(name="snakd",
      version=version,
      description='Skeleton for tornado on twisted',
      author='Kevin Etienne',
      author_email='geoke@pasunclou,com',
      url='http://www.python.org/sigs/distutils-sig/',
      packages=['snakd', 'snakd.test'],
      install_requires=[
          'Twisted',
          'tornado',
          'zope.interface',
      ]
     )
