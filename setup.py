from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str):
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "").strip() for req in requirements]
        requirements = [req for req in requirements if req != "-e ."]
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Pushkar Shahi',
    author_email='riseinspirethrive2008@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)