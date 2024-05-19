# 0x00. AirBnB clone - The console
## Project Description


### First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building our first full web application: the AirBnB clone.

In this project, we take the important first and important step to building a full fleshed web application.

We hope to integrate the learnings from this project with with all other following projects in the coming future:
- HTML/CSS templating, database storage, API, front-end integration…

Each task of the project was linked to the next and helped us achieve the
following objectives:

	* put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
	* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
	* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
	* create the first abstracted storage engine of the project: File storage.
	* create all unittests to validate all our classes and storage engine

### What’s a command interpreter?
The console is exactly the same as the shell but has a limited use-case. 
The specific use-case for this console is to enable managing the objects of our project using the CRUD operations:
	* Create a new object (ex: a new User or a new Place)
	* Retrieve an object from a file, a database etc…
	* Do operations on objects (count, compute stats, etc…)
	* Update attributes of an object
	* Destroy an object

### Project Requirements
#### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version `2.8.*`)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#### Python Unit Tests
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* All your test files should be inside a folder `tests`
* You have to use the unittest module
* All your test files should be python files (extension: `.py`)
* All your test files and folders should start by `test_`
* Your file organization in the tests folder should be the same as your project
* e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
* e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
* All your tests should be executed by using this command: `python3 -m unittest discover tests`
* You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### Description of the command interpreter
#### In interactive mode the samples below details the following:
* How to start the console
* How to use it
* Some examples
```
	$ ./console.py
	(hbnb)
	help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb)
	(hbnb)
	(hbnb) quit
	$
```

#### In non-interactive mode the samples below detail the following:
* How to start the console
* How to use it
* Some examples
```
	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb)
	$
```

All tests passed for non-interactive mode as shown below: 
`$ echo "python3 -m unittest discover tests" | bash`

## Project Creators: See Authors list
