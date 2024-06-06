from setuptools import setup, find_packages

setup(
    name="tipi-data",
    version="1.1.0",
    description="TIPI Data",
    url="https://github.com/politicalwatch/tipi-data",
    author="pr3ssh",
    packages=find_packages(),
    install_requires=[
        "marshmallow==3.21.2",
        "marshmallow-mongoengine==0.31.2",
        "mongoengine==0.28.2",
        "python-pcre==0.7",
        "natsort==7.1.1",
        "python-slugify==8.0.4",
    ],
)
