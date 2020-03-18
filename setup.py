from setuptools import setup, find_packages

setup(
    name='tipi-data',
    version='1.0.0',
    description='TIPI Data',
    url='https://github.com/politicalwatch/tipi-data',
    author='pr3ssh',
    packages=find_packages(),
    install_requires=[
        'marshmallow==2.19.2',
        'marshmallow-mongoengine==0.9.1',
        'mongoengine==0.16.2',
        'python-pcre==0.7',
        'natsort==7.0.1'
    ],
)
