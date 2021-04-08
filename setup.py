from setuptools import setup

setup(
    name="hue",
    version='0.1',
    py_modules=['api'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hue=api:cli
    ''',
)
