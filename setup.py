from setuptools import setup, find_packages


with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

setup(
    name="dalia",
    version="0.2.2",
    description="Goddess of fate, giver and taker of goods",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    author="Brewster Malevich",
    author_email="bmalevich@rhg.com",
    url="https://github.com/brews/dalia",
    packages=find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    install_requires=["numpy", "pyyaml", "anytree"],
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
    extras_require={
        "test": ["pytest"],
        "dev": ["pytest", "pytest-cov", "wheel", "flake8", "pytest", "black", "twine"],
        "doc": ["sphinx", "sphinx_rtd_theme", "numpydoc", "ipython"],
    },
)
