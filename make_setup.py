import os
import platform
import shutil

package_name = 'vardy_message'
author_name = 'Siddhant Rao'
author_email = 'sid96@live.com'
version_number = '0.0.1'
url = 'none'
description = 'A secret message from Jamie Vardy'
protected_files = ['setup.py', 'make_setupfiles.py','upload_repo.py']

def move(file):
    """
    Moves a file from the directory the program is being run into the directory
    named 'package-name'
    """
    destination = package_name
    shutil.move(file,destination)


def file_creater(package_name, author_name, author_email, version_number, url, description):
    """
    Takes informational arguments such as name of the python package, name of the author
    and creates the necessary files to convert a directory into a PyPI package for upload.
    """
    #Creates the package directory
    if not os.path.exists(package_name):
        os.mkdir(package_name)
    init_path = os.path.join(package_name, '__init__.py')
    f_init = open(init_path, "w+")
    f_init.close()

    directory = (os.listdir())
    for each in directory:
        if (('.py' in each) and (each not in protected_files)):
            if not (os.path.exists((os.path.join(package_name, each)))):
                print(each)
                move(each)
            
    #Creates the unit tests directory
    if os.path.exists('tests'):
        os.rmdir('tests')
    os.mkdir('tests')

    #Creates the file to tell build tools what system you are using

    if os.path.exists('pyproject.toml'):
        os.remove('pyproject.toml')

    f_toml = open("pyproject.toml","w+")
    f_toml.write('[build-system] \n')
    f_toml.write('requires = ["setuptools>=42", "wheel"] \n')
    f_toml.write('build-backend = "setuptools.build_meta" \n')
    f_toml.close()

    #Create setup configuration file (static cfg and dynamic py)

    if os.path.exists('setup.cfg'):
        os.remove('setup.cfg')

    f_cfg = open('setup.cfg', 'w+')
    f_cfg.write('[metadata]\n')
    f_cfg.write('name = ' + package_name + author_name + '\n')
    f_cfg.write('version = ' + str(version_number)+ '\n')
    f_cfg.write('url = ' + url+ '\n')
    f_cfg.write('author = ' + author_name + '\n')
    f_cfg.write('author_email = ' + author_email + '\n')
    f_cfg.write('classifiers = \n')
    f_cfg.write('   Programming Language :: Python :: 3 \n')
    f_cfg.write('   License :: OSI Approved :: MIT License \n')
    f_cfg.write('   Operating System :: OS Independent \n')
    f_cfg.write(' description =  ' + description + '\n')
    f_cfg.write(' long_description = file: README.md\n')
    f_cfg.write(' long_description_content_type = text/markdown\n')
    f_cfg.write(' [options]\n')
    f_cfg.write(' python_requires = >=3.6\n')
    f_cfg.close()

    if os.path.exists('setup.py'):
        os.remove('setup.py')

    namepack = package_name + '-' + author_name
    f_dyn = open('setup.py', 'w+')
    f_dyn.write('import setuptools\n')
    f_dyn.write('with open("README.md", "r", encoding="utf-8") as fh:\n')
    f_dyn.write('   long_description = fh.read()\n')
    f_dyn.write('setuptools.setup(\n')
    f_dyn.write('   name = "' + namepack + '",\n')
    f_dyn.write('   version = "' + str(version_number) + '",\n')
    f_dyn.write('   url = "' + url + '",\n')
    f_dyn.write('   author = "' + author_name + '",\n')
    f_dyn.write('   author_email = "' + author_email + '",\n')
    f_dyn.write('   description =  "' + description + '",\n')
    f_dyn.write('   long_description = long_description,\n')
    f_dyn.write('   long_description_content_type = "text/markdown",\n')
    f_dyn.write('   packages=setuptools.find_packages(),\n')
    f_dyn.write('   classifiers = [\n')
    f_dyn.write('       "Programming Language :: Python :: 3",\n')
    f_dyn.write('       "License :: OSI Approved :: MIT License",\n')
    f_dyn.write('       "Operating System :: OS Independent" ],\n')
    f_dyn.write('   python_requires = ">=3.6")\n')
    f_dyn.close()



if __name__ == "__main__":

    file_creater(package_name, author_name,
     author_email, version_number, url, description)
    









