from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This Function will return the list the requirement
    """
    hypen = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # For removing \n from each line
        requirements = [replace("\n","") for req in requirements]
        # for removing -e . from requirements
        if hypen in requirements:
            requirements.remove(hypen)
    return requirements


setup(
    name="Student_Proj",
    version= "0.0.1",
    author="Umar", 
    author_email="mominumar57@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)