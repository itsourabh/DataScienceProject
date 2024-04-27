from typing import List

from setuptools import find_packages, setup


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        [req.replace('\n',"") for req in requirements]
        
    return requirements










setup(
    name='DataScienceProject',
    version='0.1',
    author='Sourabh',
    author_email='sg9003229@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    
)