#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    work
    ~~~~

    Web design and development by Vital Kudzelka

    :copyright: (c) 2016 by Vital Kudzelka <vital.kudzelka@gmail.com>
    :license: MIT
"""
import io
import os
from setuptools import (
    find_packages,
    setup,
)

from work import (
    __version__,
    cli,
)


def read(*parts):
    try:
        return io.open(os.path.join(*parts), 'r', encoding='utf-8').read()
    except IOError:
        return ''


requirements = read('requirements', 'main.txt').splitlines()
tests_require = read('requirements', 'test.txt').splitlines()

setup(
    name='work',
    version=__version__,

    author='Vital Kudzelka',
    author_email='vital.kudzelka@gmail.com',

    url='https://github.com/vitalk',
    description='Web design and development by Vital Kudzelka',
    long_description=read('README'),
    license='MIT',

    packages=find_packages(exclude=['docs', 'tests']),
    zip_safe=False,
    platforms='any',
    install_requires=requirements,
    tests_require=tests_require,
    test_suite='tests',
    cmdclass={
        'freeze': cli.freezer.freeze,
        'serve': cli.serve.run,
        'test': cli.test.pytest,
    },

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Pypi will refuse to accept packages with unknown classifiers, so
        # the following line prevents me from uploading private package to
        # pypi. Just remove this line before publish.
        'Private :: Do Not Upload',
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
