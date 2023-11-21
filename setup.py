# setup.py
from setuptools import setup, find_packages

setup(
    name='project_two',
    version='0.5',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'lxml',
        'requests',
        'beautifulsoup4'
    ]
)
