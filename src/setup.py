import setuptools

setuptools.setup(
    name="cost-functions",
    packages=setuptools.find_packages(where="python"),
    package_dir={"": "python"},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires=["z-quantum-core",],
)
