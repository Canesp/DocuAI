from setuptools import setup, find_packages

setup(
    name='DOCUAI',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'rich',
        'keyring',
    ],
    entry_points={
        'console_scripts': [
            'DOCUAI = DOCUAI.main:main',
        ],
    },
)
