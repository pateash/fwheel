#!/usr/bin/env python
from setuptools import setup, find_packages




setup(
    name='fwheel',
    version='0.0.1.dev0',
    description="generate fat wheel similar to fat jar in java",
    # long_description=open(r'doc/README.rst').read(),
    author='Ashish Patel',
    author_email='ashishpatel0720@gmail.com',
    install_requires=['argparse'],
    # readme=r"doc\Readme.rst",
    license='MIT',
    # package_data={
    #     "fat_wheel": ["template/*.py", "template/*.txt"]
    # },
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "fatwheel = fat_wheel.fat:main"
        ]
    }
)
