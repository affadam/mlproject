from setuptools import find_packages,setup
from typing import List


HYPNE_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPNE_DOT in requirements:
            requirements.remove(HYPNE_DOT)



setup(

    name = 'mlproject',
    version = '0.0.1',
    author = 'Hariram',
    author_email='hariramct7@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)