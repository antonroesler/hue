from setuptools import setup

setup(
    name="hue",
    version='0.0',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hue=main:cli
    ''',
)