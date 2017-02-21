from setuptools import setup

setup(
    name='sanic-admin',
    version='0.0.3',
    author='38elements',
    description='sanic-admin is a command line tool for automatically restarting sanic.',
    license='MIT License',
    url='https://github.com/38elements/sanic-admin',
    install_requires=[
        'watchdog>=0.8.3'
    ],
    packages=[
        'sanic-admin'
    ],
    keywords='sanic',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers'
    ]
)
