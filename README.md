# gomoku_python
An example application for experimenting with TDD and refactoring

## Setup
You will need to install [Python 2.7](https://www.python.org/downloads/release/python-2713/) 
  
### Install virtualenv
virtualenv is a tool to create isolated Python environments. 
virtualenv creates a folder which contains all the necessary  
executables to use the packages that a Python project would need.  
`$ pip install virtualenv`
`$ mkdir tdd_kurs; cd tdd_kurs`
`$ git clone git@github.com:Softhouse/gomoku_python.git` 
`$ virtualenv my_virtenv`

### Start virtualenv
`$ source my_virtenv/bin/activate`  

### Install pygame
Install [Pygame](http://pygame.org/) first to run this program  
`(virt_env)$ pip install pygame`

## Run tests
`(virt_env)$ python -m unittest test.test_gomoku`

## Run game GUI
`(virt_env)$ cd app; python main.py` 

## Exit virtualenv
To quit the virtual environment in your shell
`$ deactivate`
