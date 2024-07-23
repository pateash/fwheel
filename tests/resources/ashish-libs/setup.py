from setuptools import setup, find_packages

setup(
    name="ashish-libs",
    version="0.1",
    packages=find_packages(),
    package_data={"ashish_libs": ["vendor/**"]},
    include_package_data=True,
)
