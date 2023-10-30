import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent.resolve()

# 以下是 package 資訊
PACKAGE_NAME = "TCS34087"
AUTHOR = "SamHsiao6238"
AUTHOR_EMAIL = "samhsiao6238@gmail.com"
URL = "https://github.com/samhsiao6238/TCS34087_Lib.git"
DOWNLOAD_URL = ""  # 
LICENSE = "MIT"
VERSION = "0.1"
DESCRIPTION = "A library for TCS34087 sensor"

# README.md 文件
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf8")
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'smbus',
    'RPi.GPIO'
]

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
)
