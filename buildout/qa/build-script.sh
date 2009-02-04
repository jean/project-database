#!/bin/bash
#Assumptions:
#   PIL is installed in the zope user account Python
#   Run the script in ~/instances/qa.unep

echo "=======================Setup plone"
/home/zope/Python-2.4.4/bin/paster create -t plone3_buildout .
echo
echo "=======================Setup buildout"
rm buildout.cfg
svn export http://project-database.googlecode.com/svn/buildout/qa/buildout.cfg
/home/zope/Python-2.4.4/bin/python bootstrap.py
echo
echo "=======================run buildout"
./bin/buildout -v
