from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Cocotb testbench functions'

# Setting up
setup(
    name="cocotb_functions",
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['cocotb'],
    keywords=['python', 'cocotb']
)
