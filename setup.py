from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='json-regex-difftool',

    version='0.2',

    description='A tool for doing a comparison or difference of JSON documents'
                'with regular expression support',

    # The project's main homepage.
    url='https://github.com/bazaarvoice/json-regex-difftool.git',

    # Author details
    author='Clayton Stout',
    author_email='clayfstout@gmail.com',

    # Choose your license
    license='Apache Software License',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Internet :: Log Analysis',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2.7',
    ],

    keywords='JSON, regular expressions, regex, diff, difftool',

    packages=find_packages(exclude=['tests*']),

    install_requires=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'json-regex-difftool=jsondiff:main',
        ],
    },
)