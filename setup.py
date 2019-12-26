from setuptools import setup, find_packages

setup(
    name='tipi-data',
    version='1.0.0',
    description='TIPI Data',
    url='https://github.com/politicalwatch/tipi-data',
    author='pr3ssh',
    packages=find_packages(),
    install_requires=[
        'mongoengine',
    ],
)
