""" Setup ariadna module """

from setuptools import setup

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name='ariadna',
    packages=['ariadna'],
    version='0.0.2b',
    license='MIT',
    description='A library of featureful collection objects providing path-like keys',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='David Cabrera',
    author_email='dacabdi@gmail.com',
    url='https://github.com/dacabdi/ariadna',
    download_url='https://github.com/dacabdi/ariadna/archive/v0.0.2b.tar.gz',
    keywords=[
        'caja',
        'dict',
        'sequence',
        'path',
        'descriptor',
        'set'
    ],
    install_requires=[
        'frozendict'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
