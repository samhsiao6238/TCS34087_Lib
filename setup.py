from setuptools import setup, find_packages

setup(
    name='TCS34087',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 外部模組
        'smbus',
        'RPi.GPIO'
    ],
    author='Sam6238',
    author_email='gsam6238@gmail.com',
    description='A library for TCS34087 sensor',
    keywords='TCS34087 sensor raspberry pi',
    url='https://github.com/yourusername/TCS34087_lib',  # GitHub 連結
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ]
)
