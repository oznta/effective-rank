import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "effectiverank",
    version = "1.0",
    description = "Calculation of the effective rank of a matrix",
    author = "",
    author_email = "",
    license = "MIT",
    keywords = "rank effective timeseries correlation",
    url = "https://github.com/oznta/effectiverank",
    packages=['effectiverank'],
    install_requires=['numpy>= 1.11.1',
                      'pandas>1.0.0',
                      'scikit-learn>1.0.0',
                      'importlib',
                      'yfinance>=0.1.74'                     
                      ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Science/Research',
        "Topic :: Statistics",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.9'
    ],
    long_description=read('README.md'),
)
