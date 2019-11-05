import os
import sys
from setuptools import setup

project_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(project_dir, 'README.md'), 'r') as f:
    long_description = f.read()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='gooee-statsd',
    version='1.0.0',
    package_dir={'': 'src'},
    packages=['gooee_statsd'],
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/GooeeIOT/cloud-python-statsd',
    license='MIT',
    author='Gooee Limited',
    author_email='cloud-backend@gooee.com',
    description='Useful abstractions for interacting with statsd the Gooee way.',
    long_description=long_description,
    install_requires=['datadog>=0.28.0,<0.31.0'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=['python', 'statsd', 'graphite'],
)
