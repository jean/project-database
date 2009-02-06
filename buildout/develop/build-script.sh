#!/bin/bash
#Assumptions:
# The current user home folder contains:
#   repos/google/project-database/...
#   instances folder (WITHOUT a folder called unep)
#   PIL is untarred in src/Imaging-1.1.6
#   python-reportlab is already installed in the system python

REPOS=~/repos/google/project-database
INSTANCE=~/instances
SRC=~/src

echo
echo "=======================Setup python"
cd $INSTANCE
virtualenv --no-site-packages unep
source unep/bin/activate
python $SRC/Imaging-1.1.6/setup.py install
echo "=======================Setup Reportlab"
ln -s /usr/lib/python2.4/site-packages/reportlab unep/lib/python2.4/site-packages/reportlab
echo
echo "=======================Setup plone"
easy_install ZopeSkel
paster create -t plone3_buildout unep
echo
echo "=======================Setup buildout"
rm unep/buildout.cfg
ln -s $REPOS/buildout/develop/buildout.cfg unep/
cd unep
python bootstrap.py
echo
echo "=======================Setup links to dev trunks"
ln -sf $REPOS/unep.project-database/trunk products/ProjectDatabase
ln -sf $REPOS/3rdparty/DataGridField/trunk products/DataGridField
ln -sf $REPOS/unep.policy/trunk/unep.policy src/unep.policy
ln -sf $REPOS/unep.theme/trunk/unep.theme src/unep.theme
echo
echo "=======================run buildout"
./bin/buildout -v
