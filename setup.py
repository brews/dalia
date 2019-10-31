from setuptools import setup, find_packages


with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "numpy",
    "pyyaml",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "flake8",
    "pytest",
]

setup(
    name="dalia",
    version="0.1.1",
    description="Goddess of fate - giver and taker of goods",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    author="Brewster Malevich",
    author_email="bmalevich@rhg.com",
    url="https://github.com/brews/dalia",
    packages=find_packages(include=["dalia"]),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords="dalia",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Sociology",
    ],
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
