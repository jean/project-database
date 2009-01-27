#!/bin/bash
#Assumptions:
# The current user home folder contains:
#   repos/google/project-database/...
#   instances folder (WITHOUT a folder called unep)
#   PIL is untarred in src/Imaging-1.1.6 

echo
echo "=======================Setup python"
cd ~/instances
virtualenv --no-site-packages unep
source unep/bin/activate
python ~/src/Imaging-1.1.6/setup.py install
echo
echo "=======================Setup plone"
easy_install ZopeSkel
paster create -t plone3_buildout unep
echo
echo "=======================Setup buildout"
rm unep/buildout.cfg
ln -s ~/repos/google/project-database/buildout/develop/buildout.cfg unep/
cd unep
python bootstrap.py
echo
echo "=======================Setup links to dev trunks"
ln -sf ~/repos/google/project-database/unep.project-database/trunk products/ProjectDatabase
ln -sf ~/repos/google/project-database/3rdparty/DataGridField/branches/calendarcolumn products/DataGridField
ln -sf ~/repos/google/project-database/unep.policy/trunk/unep.policy src/unep.policy
ln -sf ~/repos/google/project-database/unep.theme/trunk/unep.theme src/unep.theme
echo
echo "=======================run buildout"
./bin/buildout -v
