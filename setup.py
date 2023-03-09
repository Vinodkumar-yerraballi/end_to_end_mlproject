from setuptools import find_packages,setup
from typing import List

hypen_d_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace('\n'," ") for req in requirments]
        if hypen_d_dot in requirments:
            requirments.remove(hypen_d_dot)
        return requirments




setup(
    name='mlproject',
    version='0.0.1',
    author='Vinod kumar',
    author_email='vinodkumar9676150@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)