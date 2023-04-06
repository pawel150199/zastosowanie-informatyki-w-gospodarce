import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


dependencies = open("requirements.txt", "r").read().splitlines()

setuptools.setup(
    name="Harcownik API",
    version="1.0",
    description="API for harcownik scout application",
    author="Pawel Polski",
    author_email="pawel.polski99@gmail.com",
    long_description=long_description,
    packages=setuptools.find_packages(where="src"),
    long_description_content_type="text/markdown",
    install_requires=dependencies,
    platforms="any",
    py_modules=["logger"],
    package_dir={"": "src"},
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["termcolor==1.1.0 "],
)
