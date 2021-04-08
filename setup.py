from setuptools import setup

setup(
    name="hue",
    version='0.1',
    py_modules=['src'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hue=src.api:cli
    ''',
)
