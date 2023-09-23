'''
This file allow to package the project to allow the distribution with pip
'''
''''''
from setuptools import find_packages, setup
from typing import List 

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function allows reading the requirements.txt file and returns a list of requirements.
    '''
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "student_performance_project"
AUTHOR_USER_NAME = "LuisOlcay20"
AUTHOR_EMAIL = "luis.olcay@uc.cl"

setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="End to end ML project",
    long_description=long_description,
    long_description_content_type="text/markdown",  # changed to long_description_content_type
    url="https://github.com/LuisOlcay20/students_performance_project",  # added missing quote at the start
    project_urls={
        "Bug Tracker": "https://github.com/LuisOlcay20/students_performance_project/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),  # found packages in src folder
    install_requires=get_requirements("requirements.txt"),
)


