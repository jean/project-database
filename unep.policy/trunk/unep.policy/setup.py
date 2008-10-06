from setuptools import setup, find_packages
import os

version = '0.1 build 1'

setup(name='unep.policy',
      version=version,
      description="UNEP Project Database configuration product",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='UNEP project database configuration',
      author='Jurgen Blignaut',
      author_email='jurgen@upfrontsystems.co.za',
      url='https://project-database.googlecode.com/svn/unep.policy/trunk',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['unep'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
