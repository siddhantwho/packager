# packager
[![Python: 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://pypi.org/project/socceraction)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://en.wikipedia.org/wiki/MIT_License)

A simple tool to build PyPI packages and upload them
 
- A make_setup program that automatically constructs the required setup files given the metadata information
- An upload_repo program that builds the distrubution packages and runs the commands to upload the repository to PyPI
 
# Instructions

In a directory containing the following file structure, copy the make_setup.py and upload_repo.py files.

```
project
│   README.md
│   LICENSE
│
└───package
│   │   code.py
│   │   morecode.py

```

or 

```
project
│   README.md
│   LICENSE
│   code.py

```
Open the make_setup.py file and edit the values for the following
```ruby
package_name = 'Your_package_name_here'
author_name = 'Author Name'
author_email = 'author@host.com'
version_number = '0.0.1'
url = 'https://github.com/author/package'
description = 'Short description of the package'
program_language = 'Python :: 3' 
repo_license = 'MIT License'
operating_system = 'OS Independent'

```

and then run

```sh
python make_setup.py
```

This should create the required set up files in order to build the distribution. At this point you may check the setup files to see if the information is reflected correctly. If not, the make_setup program can be edited and re-run or the setup files can be modified directly. Next run

```sh
python upload_repo.py
```
This command will install the python module build and twine if not already installed and create the build files. The repository will then be uploaded to PyPI; you will have an option to upload to the test server first. The program will then ask you for your PyPI authentication credentials.

Your module should now be available on PyPI's server and can be installed using pip!

 
