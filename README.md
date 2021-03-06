# gomoku_python
An example application for TDD and refactoring using the board game [Gomoku](https://en.wikipedia.org/wiki/Gomoku)

## Setup
You will need to have [Python 2.7](https://www.python.org/downloads/release/python-2713/) installed
A good source to learn about Python is the [Python Documentation](https://docs.python.org/2.7/).

Also the packet manager [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) is needed. If you have `pip` installed
you should be able to

    $ pip --version
    pip 9.0.1
  
### Install virtualenv
[virtualenv](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) is a tool to create isolated Python environments. 
virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.  

    $ pip install virtualenv
    $ mkdir tdd_kurs
    $ cd tdd_kurs
    $ git clone git@github.com:Softhouse/gomoku_python.git 
    $ virtualenv my_virtenv

### Running virtualenv
Start `virtualenv` so all dependencies are installed inside it

    $ source my_virtenv/bin/activate
    
After the lab you can quit the virtual environment by

    $ deactivate
    
### Install pygame
With `virtualenv` running, install [Pygame](http://pygame.org/)   

    (virt_env)$ pip install pygame

A [Pygame cheat sheet](https://inventwithpython.com/blog/2011/10/07/pygame-cheat-sheet/) explains the
code components of Pygame, read it if you are interested. Pygame is necessary to run the game, but not to
run the tests.

## Run tests

    (virt_env)$ python -m unittest test.test_model

Read more on how to create Python [unittest](https://docs.python.org/2.7/library/unittest.html#module-unittest)s

## Run game

Run the game through its GUI

    (virt_env)$ cd app; python main.py

## Lab
When you write code that accesses a token or cell, the order is first **row** then **column** throughout the code,
for example:

    row, col = pos

## Code coverage
If you like you can measure [Code coverage](https://en.wikipedia.org/wiki/Code_coverage) to see how much of 
the production code is exercised by the tests.

    (my_virtenv)$ pip install coverage
    
    $ python -m coverage --help
    Coverage.py, version 4.3.4 with C extension

### Run coverage ###
First check you are in the root of repo 

    $ ls
    README.md	app		my_virtenv	solutions	test
 
Then run your tests through the tool

    $ python -m coverage run -m unittest discover
    
Create a report

    $ python -m coverage html
    
Then show it in your browser (choose `open` or web browser name as suitable to your environment)

    $ open htmlcov/index.html
    $ firefox htmlcov/index.html

To clear between runs, do:

    $ python -m coverage erase
