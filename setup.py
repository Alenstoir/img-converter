import os
from pathlib import Path

from cx_Freeze import Executable, setup
from setuptools import find_packages


def get_version():
    with open(Path(__file__).parent / "img_converter/VERSION", encoding="utf8") as fp:
        return fp.read()


def long_description():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, "README.rst"), "r", encoding="utf8") as fh:
        return fh.read()


ver = get_version()
executables = [
    Executable(
        'img_converter/ui/ui.py',
        target_name="ImgConverter",
        base="Win32GUI",
        icon="icon.ico",
        shortcut_name='Alenstoir Image Converter',
        shortcut_dir='ProgramMenuFolder'
    ),
]

excludes = [
    'unicodedata', 'unittest', 'email', 'html', 'http', 'urllib',
    'xml', 'pydoc', 'doctest', 'argparse', 'datetime', 'zipfile',
    'subprocess', 'pickle', 'locale', 'calendar',
    'base64', 'gettext',
    'bz2', 'getopt', 'stringprep',
    'quopri', 'copy', 'imp', 'packaging'
]

includes = ['logging', 'contextlib', 'string', 'fnmatch', 'linecache', 'tokenize', 'threading']
zip_include_packages = [
    'collections', 'logging', 'encodings', 'importlib', 'tkinter', 'PIL', 'contextlib', 'string', 'fnmatch',
    'linecache', 'tokenize', 'threading'
]
options = {
    'build_exe': {
        'include_msvcr': False,
        'includes': includes,
        'excludes': excludes,
        'zip_include_packages': zip_include_packages,
    }
}

setup(
    name="alenstoir-img-converter",
    version=ver,
    author="Alenstoir",
    author_email="alenstoir@yandex.ru",
    license="MIT",
    description="Img converter.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Alenstoir/img-converter",
    python_requires=">=3.8,<3.13",
    install_requires=[
        "pillow",
    ],
    entry_points={
        "console_scripts": [
            "alen-converter = img_converter.ui.ui:main",
        ]
    },
    executables=executables,
    options=options
)
