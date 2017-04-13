# gomoku_python
An example application for experimenting with TDD and refactoring

## Setup
You will need to install [Python 2.7](https://www.python.org/downloads/release/python-2713/) 
  

### virtualenv
virtualenv is a tool to create isolated Python environments. 
virtualenv creates a folder which contains all the necessary  
executables to use the packages that a Python project would need.  
`$ pip install virtualenv`  
`$ cd project_folder you cloend`  
`$ virtualenv my_project`  
`$ source my_project/bin/activate`  

### pygame
Install [Pygame](http://pygame.org/) first to run this program  
`(virt_env)$ pip install pygame`

### Unittest framework
Install the python nosetest framework.  
`(virt_env)$ pip install nose`

## Running
`(virt_env)$ python main.py` 

## Test
`(virt_env)$ nosetests example_unit_test.py`