from setuptools import setup

setup(name='dumbno',
    version='0.4.0',
    zip_safe=True,
    py_modules = ["dumbno"],
    install_requires=[
        "jsonrpclib",
    ],
    entry_points = {
        'console_scripts': [
            'dumbno = dumbno:main',
        ]
    }
)
