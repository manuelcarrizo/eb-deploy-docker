#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='eb-deploy-docker',
    version='0.0.1',
    description='A command line utility to deploy to Elastic Beanstalk Docker platforms',
    url='https://github.com/manuelcarrizo/eb-deploy-docker',
    author='Manuel Carrizo',
    author_email='manuelcarrizo@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    packages=find_packages(),
    install_requires=[
        'awsebcli',
        'boto3',
        'pyaml'
    ],
    entry_points={
        'console_scripts': [
            'eb-deploy-docker=src.eb_deploy_docker:main'
        ]
    }
)