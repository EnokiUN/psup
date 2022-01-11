import re

from setuptools import setup

version = ""
with open("psup/__init__.py") as f:
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
    if match is not None:
        version = match.group(1)
    else:
        raise RuntimeError("version is not set")

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

extra_requirements = []

readme = ""
with open("README.rst") as f:
    readme = f.read()

setup(
    name="psup",
    author="EnokiUN",
    url="https://github.com/EnokiUN/psup",
    project_urls={
        "Documentation": "https://psup.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/enokiun/psup/issues",
    },
    download_url="https://github.com/EnokiUN/psup/archive/refs/tags/Release-0-1-1-5a.tar.gz",
    version=version,
    license="MIT",
    packages=["psup"],
    install_requires=requirements,
    extra_requires=extra_requirements,
    description="A simple library for making complex stories and games.",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    python_requires=">=3.8.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
