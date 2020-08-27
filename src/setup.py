import setuptools
import os

setuptools.setup(
    name="trying-new-cost-function",
    version="0.2.0",
    url="https://github.com/luisguiserrano/trying-new-cost-function",
    packages=setuptools.find_namespace_packages(include=['zquantum.*']),
    packages = setuptools.find_packages(where = "python")
    package_dir={'' : 'python'},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    #install_requires=[
    #    'z-quantum-core',# 'trying-new-cost-function'
    #]
)