from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str)-> List[str]:
    HYPEN_E_DOT = '-e .'
    requirements = []

    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = 'comment_toxicity_classfier',
    version = '0.0.3',
    author = 'WiznikVibe',
    author_email = 'nikhilshetty00@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

) 