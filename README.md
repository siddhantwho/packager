# packager
[![Python: 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://pypi.org/project/socceraction)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://en.wikipedia.org/wiki/MIT_License)

A simple tool to build PyPI packages and upload them
 
- A make_setup program that automatically constructs the required setup files given the metadata information
- An upload program that builds the distrubution packages and runs the commands to upload the repository to PyPI
 
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

 
