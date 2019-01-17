import os
import pathlib
from setuptools import setup, find_packages


setup(
    name='CSGVulcan',
    version='0.1.dev',
    author='CSG Data Science Dept.',
    author_email='csgdatascience01@gmail.com',
    packages=find_packages(),
    license='GPL',
    keywords='vulcan csg datascience hca',
    long_description=open('README.md'),
    install_requires=[
        'Flask >= 1.0.2'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPL License",
    ],
)
