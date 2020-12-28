#!/usr/bin/env python3

from setuptools import setup

setup(
    name='gantt-tool',
    version='0.1.0',
    url='http://github.com/ReverentEngineer/gantt-tool',
    license='MIT',
    author='Jeff Caffrey-Hill',
    author_email='jeff@caffreyhill.com',
    description='A YAML-based Gantt chart generator',
    python_requires='>=3.6',
    platforms=['any'],
    py_modules=['gantt_tool'],
    entry_points={
        'console_scripts': [
            'gantt-tool = gantt_tool:main',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Utilities',
    ],
