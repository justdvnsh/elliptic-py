import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ellipticpy",
    version="0.0.1",
    author="Divyansh Dwivedi",
    author_email="justdvnsh2208@gmail.com",
    description="A fast implementation of Elliptic - Curve Cryptography in pure Python. ( Port of Elliptic-JS )",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/justdvnsh/elliptic-py",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)