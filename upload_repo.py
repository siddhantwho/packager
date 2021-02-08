import os

def ask():
    test = input('Would you like to upload this to PyPI\'s TEST repository? y/n')
    
    if (test == 'y'):
        answer = True
        return answer
    elif (test == 'n'):
        answer = False
        return answer
    else:
        print ('I didn\'t understand that')
        ask()

def build():
    """
    Uses the TOML and setup files from the make_setupfiles.py program to build a the
    dist/ and build/ directories and populate them with the distribution files
    """

    #run build commands in shell, requires the latest version of build
    os.system('python -m pip install --upgrade build --user')
    os.system('python -m build')

def upload(test_PyPI):
    
    #uploading the created distributions to the PyPI archive, requires twine
    os.system('python -m pip install --upgrade twine --user')
    if (test_PyPI):
        os.system('python -m twine upload --repository testpypi dist/*')
    if (not test_PyPI):
        os.system('python -m twine upload dist/*')

if __name__ == "__main__":

    build()
    test_repo = ask()
    upload(test_repo)
    

