from distutils.command import build

from setuptools import setup
from setuptools.command import develop

setup(
    name='azure-functions-stub-extension',
    version='1.0.0',
    description='Python Language Extension Stub',
    author="Roger Zeng",
    author_email="hazeng@microsoft.com",
    keywords="azure azurefunctions python",
    url="https://github.com/Hazhzeng/azure-functions-stub-extension",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Environment :: Web Environment',
    ],
    license='MIT',
    packages=['azure_functions_stub_extension'],
    install_requires=[
        'azure-functions'
    ],
    extras_require={},
    include_package_data=True
)
