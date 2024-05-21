from setuptools import setup, find_packages
from spins2 import __version__

setup(
    name='spins2',
    version=__version__,
    author='kan',
    author_email='luokan@mail.ecust.edu.cn',
    python_requires=">=3.8",
    license='MIT',
    license_files=('LICENSE.txt',),
    platforms=['Unix', 'Windows'],
    keywords='Monte Carlo Simulation Ising Model',
    description='A Monte Carlo Simulation Code for the Phase Transition in 2D/3D Magnetic Materials.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lkccrr/spins2',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3 :: Only",
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
    install_requires=[
        'numba>=0.54.0',
        'numpy>=1.22.0',
        'matplotlib>=3.6.0'
    ],
    entry_points={
        'console_scripts': ['spins2=spins2.wrapper:main']
    },
    packages=find_packages(),
    include_package_data=True
)

