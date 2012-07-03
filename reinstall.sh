source venv/bin/activate &&
if [ $(pip freeze | grep Projy | wc -w ) -eq 1 ]; then
    pip uninstall -q -y Projy
fi &&
python setup.py sdist &&
pip install -q dist/Projy-0.1.2.tar.gz &&
rm -rf dist Projy.egg-info
