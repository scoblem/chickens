import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()

setup(
    name='chickens',
    version='1.7',
    description='chickens',
    long_description=readme,
    author='Mark Scoble',
    author_email='scoble.mr@gmail.com',
    url='https://github.com/Necrolisk/chickens',
    packages=['chickens'],
    package_dir={'chickens': 'chickens'},
    include_package_data=True,
    install_requires=[
        'egg'
    ],
    zip_safe=False,
    keywords=['chicken', 'CHICKEN', 'CHICKENS', 'chickens'],
    classifiers=[],
)
