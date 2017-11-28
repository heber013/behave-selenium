import sys
from setuptools import find_packages, setup

assert sys.version_info >= (3,), 'Python 3 is required'


VERSION = '1.0'


setup(
    name='automation-exercise',
    version=VERSION,
    description='Automation example',
    author='Heber Parrucci',
    author_email='heber013@gmail.com',
    url='',
    packages=find_packages(),
    package_data={
        '': []
    },
    entry_points={
        'console_scripts': [
            ''
        ]
    },
    test_suite=''
)
