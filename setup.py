from setuptools import find_packages, setup
from typing import List #This is for type hinting.

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> List[str]:
    #this function will return list of requirements
    requirements = []
    with open(file_path) as file_obj:
# with ensures the file is safely closed after reading, even if 
# an error occurs
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


    return requirements        

'''
So if requirements.txt looked like this:

nginx
Copy
Edit
numpy
pandas
scikit-learn
Then requirements would be:

python
Copy
Edit
['numpy\n', 'pandas\n', 'scikit-learn\n']
'''

'''To make sure while installing all the requirements the setup.py also
 get installed add -e .'''
setup (
    name = 'MLproject1',
    version = 1,
    author = "Vivek Kumar",
    author_email= "vivek.kumar240043@gmail.com",
    packages = find_packages(),
    # install_requires = ['pandas', 'numpy', 'seaborn'],  it'll 
    #automatically install all the lib. Writing packages every time
    # won't be easy so we'll write a function.

    install_requires = get_requirements('requirements.txt')
)

