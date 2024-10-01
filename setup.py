import os
from pathlib import Path

from setuptools import find_packages, setup


def get_version():
    with open(Path(__file__).parent / "img-converter/VERSION", encoding="utf8") as fp:
        return fp.read()


def long_description():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, "README.rst"), "r", encoding="utf8") as fh:
        return fh.read()


setup(
    name="alenstoir-img-converter",
    version=get_version(),
    author="Alenstoir",
    author_email="alenstoir@yandex.ru",
    license="MIT",
    description="Img converter.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Alenstoir/img-converter",
    packages=find_packages(exclude=["venv", "input", "output"]),
    include_package_data=True,
    python_requires=">=3.8,<3.13",
    install_requires=[
        "pillow",
    ],
    entry_points={
        "console_scripts": [
            "alen-converter = img_converter.ui.ui:main",
        ]
    },
)