from distutils.core import setup

dependencies = open("requirements.txt", "r").read().splitlines()

dist = setup(
    name="Harcownik API",
    version="1.0",
    description="API for harcownik scout application"
    author="Paweł Polski",
    author_email="pawel.polski99@gmail.com",
    long_description=open("README.md", "r").read(),
    version=__version__,
    long_description_content_type="text/markdown",
    install_requires=dependencies,
    platforms="any"
)