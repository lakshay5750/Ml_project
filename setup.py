from setuptools import find_packages,setup
from typing import List
HYPE_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function return the list of requirements.txt content
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPE_E_DOT in requirements:
            requirements.remove(HYPE_E_DOT)
    return requirements

setup(
    name='mlProject',
    version='0.0.1',
    author='Lakshay',
    author_email='lakshyavarshney62@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)