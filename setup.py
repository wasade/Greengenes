import re
import ast
from glob import glob

from setuptools import find_packages, setup

classes = """
    Topic :: Software Development :: Libraries
    Topic :: Scientific/Engineering
    Topic :: Scientific/Engineering :: Bio-Informatics
    Programming Language :: Python
    Programming Language :: Python :: 3
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

setup(name='greengenes',
      version=version,
      description="Greengenes",
      long_description="The Greengenes Reference Database and Taxonomy",
      author="Greengenes development team",
      author_email="mcdonadt@colorado.edu",
      maintainer="Greengenes development team",
      maintainer_email="mcdonadt@colorado.edu",
      url='https://github.com/greengenes/Greengenes/',
      test_suite='nose.collector',
      packages=find_packages(),
      scripts=glob('scripts/*py'),
      install_requires=['flask', 'sqlalchemy', 'flask-sqlalchemy', 'sqlite'],
      extras_require={'test': ["nose", "pep8", "flake8", "factory-boy"]},
      classifiers=classifiers,
      )
