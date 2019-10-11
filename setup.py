from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(brews): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'flake8',
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='dalia',
    version='0.0.1a1',
    description="Goddess of fate - giver and taker of goods",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    author="Brewster Malevich",
    author_email='bmalevich@rhg.com',
    url='https://github.com/brews/dalia',
    packages=find_packages(include=['dalia']),
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='dalia',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
