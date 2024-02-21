from setuptools import setup,find_packages
from typing import List


PROJECT_NAME = "MACHINELEARNINGDELIVERY"
VERSION = "0.0.1"
DESCRIPTION = "THIS IS OUR ML PROJECT IN MODULAR CODING"
AUTHOR_NAME = "NIDHISH WAKODIKAR"
AUTHOR_EMAIL = "nidhishwakodikar@gmail.com"


# REQUIREMENTS_FILE = 
HYPHEN_E_DOT="-e ."
def get_requ(REQUIREMENTS_FILE:str)->list[str]:
    with open(REQUIREMENTS_FILE) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup (
    name = PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires = get_requ("requirements.txt")
)