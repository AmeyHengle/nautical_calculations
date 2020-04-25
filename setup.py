import pathlib
from setuptools import setup,find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="nautical_calculations",
    version="1.0.1",
    description="Get all the nautical calculations here. ",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AmeyHengle/nautical_calculations",
    author="Amey Hengle",
    author_email="domainamey@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages= find_packages(exclude=("tests")),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "nautical_calculations = nautical_calculations.__main__:main",
        ]
    },
    python_requires='>=3.6'
)
