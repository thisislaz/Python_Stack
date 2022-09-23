#MODULES
    #modules are simply python files with the ".py" extension which implement a set of functions
    #modules are imported using the "import" command
    #the first time a module is loaded into a running python script, it is intialized by execvuting the code in the module once.
    #if another module in your code imports the same module again, it will not be laoded twice but once only - so local variabels inside the module act as a "singleton"; they are initialized only once
    #if we want to import "urllib.request" module, we simply import the module
# import the library
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)

    #we used a variable to refer to our module and then we called the methods using dot notation

#CREATING YOUR OWN MODULES
    #to create a module, we first create a new .py file with the module name in the same directory as the file that will import the module
    #then we import it using the "import" command and the python file name(without the .py extension)
    #for this ex, lets create a module of arithmetic operations
#modular_example/arithmetic.py
def add(x, y):
    return x + y
def multiply(x, y):
    return x * y
def subtract(x, y):
    return x - y
    
    #now make another file in the same directory as "arithmetic.py" called "calculations.py".
    #we can import the arithmetic module into "calculatioons.py" and run the functions by doing this:
#modular_example/calculations.py
import arithmetic
print(arithmetic.add(5, 8))
print(arithmetic.subtract(10, 5))
print(arithmetic.multiply(12, 6))
    #make sure the module and the file importing the module are in the same folder/directory

#STANDARD (BUILT-IN) MODULES
    #python comes with alot of builtin modules.
    #some modules are builtin into the interpreter

#EXPLORING BUILTIN MODULES
    #helpful functions in exploring the modules:
        #"dir" function -- looks for which functions are implemented in each module 
        #"help" function

#PACKAGES
    #a module is a single file(or files) that is imported under one import.
    #a "package" is a collection of modules in directories that give a package hierarchy
from my_package.subdirectory import my_functions

    #packages are namespaces which contain multiple packages and modules themselves.
        #they are directories but with a twist
sample_project
     |_____ python_file.py
     |_____ my_modules
               |_____ __init__.py
               |_____ test_module.py
               |_____ another_module.py
               |_____ third_module.py
    
    #in that example above the package name is "my_modules"

#WRITING PACKAGES
    #if we create a directory called "my_modules",which marks the package name, we can trrhen create a module inside that package called test_module
    #to use the module "test_module" we can import two ways
import my_modules.test_module
    #or
from my_modules import test_module

#__INIT__.PY FILE
    #this file was required for an older version of python
        #it was required to indicatre that the files in the folder were part of the package
    #in newer versions we only need this file if we need to cutomize what modules are available to anyone attempting to import the package
    #if we didnt want another_module or third_module to be accessible for importing, we could override the __all__ variable liek this:
#sample_project/my_modules/__init__.py
__all__ = ["test_module"]

