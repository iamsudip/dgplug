#!/usr/bin/env python
"""tweetup project"""

requirements = []

try:
    from setuptools import setup, find_packages
except ImportError:
    requirements.append('setuptools')

try:
    import fbconsole
except ImportError:
    requirements.append('fbconsole')

setup(name = 'tweetup',
    version = '0.1.4',
    description = "A script to upload photo to facebook",
    long_description = "A script to upload photo to facebook",
    platforms = ["Linux"],
    author = "iam_sudip",
    author_email = "iamsudip@programmer.net",
    url = "https://github.com/iamsudip",
    license = "MIT",
    packages = find_packages(),
    install_requires = requirements,
    dependency_links = [ 'https://pypi.python.org/pypi/fbconsole/0.3', 
                         'https://pypi.python.org/pypi/poster/0.8.1',
                       ],
    include_package_data = True,
    scripts = ['tweetup']
    )
