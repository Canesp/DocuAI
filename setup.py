from setuptools import setup, find_packages

setup(
    name='DOCUAI',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'DOCUAI = DOCUAI.src.main:main',
        ],
    },
)
