
from setuptools import setup, find_packages
from sort.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='sort',
    version=VERSION,
    description='List sorting app',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='John Doe',
    author_email='john.doe@example.com',
    url='https://github.com/johndoe/myapp/',
    license='unlicensed',
    test_suite = 'tests',
    packages=find_packages(exclude=['docs', 'ez_setup', 'tests*']),
    package_data={'sort': ['templates/*']},
    include_package_data=True,
    entry_points={"console_scripts": ["sortli=sort.main:main"]},
)
