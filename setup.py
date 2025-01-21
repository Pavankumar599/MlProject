from setuptools import find_packages,setup
from typing import List

E = '-e .'

def get_requirements(file_path:str)->List[str]:
    
    '''
    This function returns List of requirements
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if E in requirements:
            requirements.remove(E)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Pavan',
    author_email='medarametlapavankumar18@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)