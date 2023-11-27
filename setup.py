from setuptools import setup, find_packages

setup(
    name='DOCUAI',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        'openai',
        'rich',
        'keyring',
        'nbconvert',
    ],
    entry_points={
        'console_scripts': [
            'DOCUAI = DOCUAI.main:main',
        ],
    },
)
