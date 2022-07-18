from pathlib import Path

from setuptools import find_packages, setup

from version import get_version

HERE = Path(__file__).parent.resolve()

setup(
    name="evacuator",
    version=get_version(),
    description="Catch an exception and exit with an exit code",
    long_description=(HERE / "README.rst").read_text(),
    url="https://gitlab.services.mts.ru/bigdata/platform/everproject/evacuator",
    packages=find_packages(),
    author="ONEtools Team",
    author_email="onetools@mts.ru",
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
)
