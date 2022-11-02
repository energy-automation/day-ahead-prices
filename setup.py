from setuptools import setup

setup(
    name='day-ahead-prices',
    version='0.1.0',
    description='Download hourly electricity prices directly from auction houses',
    url='https://github.com/energy-automation/day-ahead-prices',
    author='Krakkus',
    author_email='krakkus@outlook.com',
    license='MIT',
    packages=['day-ahead-prices'],
    install_requires=[],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
