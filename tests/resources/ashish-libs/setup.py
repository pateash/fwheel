from setuptools import setup, find_packages

setup(
    name="ashish-libs",
    version="1.0.0",
    packages=find_packages(),
    package_data={"ashish_libs": ["vendor/**"]},
    include_package_data=True,
)
