#!/usr/bin/python
from setuptools import setup, find_packages

setup(
          name = "cryotec_server",
          version = "1.1.1",
          url = 'http://github.com/darvin/cryotec_server',
          license = 'Greedy Open Source',
          description = "Cryotec Service Server",
          author = 'Sergey Klimov',
          packages = find_packages('src'),
          package_dir = {'': 'src'},
          install_requires = ['setuptools'],
     )
