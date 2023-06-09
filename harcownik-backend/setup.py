import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Harcownik API",
    version="1.0",
    description="API for harcownik scout application",
    author="Pawel Polski",
    author_email="pawel.polski99@gmail.com",
    long_description=long_description,
    packages=setuptools.find_packages(where="src"),
    long_description_content_type="text/markdown",
    platforms="any",
    py_modules=["logger"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "alembic==1.9.1",
        "black==22.1.0",
        "emails==0.6",
        "fastapi==0.95.0",
        "Jinja2==3.1.2",
        "jose==1.0.0",
        "jwt==1.3.1",
        "psycopg2-binary==2.9.6",
        "pydantic==1.10.7",
        "pytest==7.1.2",
        "pytest-mock==3.5.1",
        "python-jose==3.3.0",
        "python-multipart==0.0.6",
        "SQLAlchemy==1.4.45",
        "typing==3.7.4.3",
        "typing_extensions==4.5.0",
        "uvicorn==0.20.0"
    ],
)
