from os.path import abspath, dirname, join

from setuptools import find_packages, setup

from version import get_version

__version__ = get_version()
SELF_PATH = abspath(dirname(__file__))

with open(join(SELF_PATH, "README.rst")) as f:
    long_description = f.read()

setup(
    name="evacuator",
    version=__version__,
    description="Catch an exception and exit with an exit code",
    long_description=long_description,
    url="https://gitlab.services.mts.ru/bigdata/platform/everproject/evacuator",
    packages=find_packages(),
    author="ONEtools Team",
    author_email="onetools@mts.ru",
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
)
