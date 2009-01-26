cd ~/instances
mkdir unep_project
cd unep_project
virtualenv --no-site-packages
source python/bin/activate
easy_install ZopeSkel
paster create -t plone3_buildout unep
rm unep/buildout.cfg
ln -s ~/repos/google/project-database/buildout/develop/buildout.cfg unep/
cd unep
python bootstrap.py
