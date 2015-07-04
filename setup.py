__author__ = 'hkar'

from distutils.core import setup

setup(
    name='Vault',
    version='0.0.1dev',
    packages=['Vault'],
    install_requires=[
        "tinys3",
        "pyyaml",
    ],
    license='GPL v3',
    long_description=open('README.md').read(),
)
