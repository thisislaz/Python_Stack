#FUNCTIONS
    #functions are a named block of code that we can execute to perform a specfic task
    #a list of instructions that we can run at anythime and as many times as we want
    #a function:
        #has a name
        #takes in parameters
        #performs a series of instructions
        #returns something afterward(will return None if hterre is no explicit return statement)
    #they are similar to receipes:
        #Specify the ingredients (variables) needed for the meal
        #Use the actual ingredients (pass arguments) when starting (invoke a function)
        #We follow the instructions step by step (function) for the ingredients (parameters) and prepare them
        #Once the food is ready we serve it up to those that are eating. (return)
    #advantages of functions:
        #reducing the duplication of code
        #breaking down complex problems into simpler peices
        #improving the clarity of code

#SYNTAX 
    #the key word "def" signifies the decalartion of a function.
    #this assigns it a name so we can "call" it later
    #'parameters' are inputs the function is expecting and appear inside the parenthesis

from webbrowser import GenericBrowser


def add(a,b):#function name :'add', parameters: a and b
    x = a+b  #process
    return x #return value: x
    #function was not 'invoked' because we did not 'call' it
    #calling is done by using the functions name followed by ()

new_val = add(3,5) #calling the add function, with arguments 3 and 5
print(new_val) # the result of the add function gets sent back to and saved into new_val
               #prints 8
    
    #some functions tkae an input and some functions dont give us an output
    #even if no output is produced, the code inside the function can alter the program known as "side effect"

#PARAMETERS AND ARGUMENTS
    #we define the inputs of functions suing parameters
def say_hi(name):
    print('hi, ' + name)

    #nothing so far, until we invoke the function

say_hi('micheal')
say_hi('anna')
say_hi('eli')
    #in the above: parameter is the 'name"
    #arguments are the answers: 'micheal' 'anna' 'eli'
    #we define parameters; we pass in arguments

#RETURNING VALUES
    #we need our function to ' return' some sort of value that we can use later in our program
    #remember the following:
        #a function call is equal to whatever that function returns

def say_hi(name):
    return 'hi '+ name
greeting = say_hi('lazaro') #the returned value fro say_hi function gets assigned to the 'greeting' variable
print(greeting)#this will output 'hi lazaro'
    #returning a value from a fucntion allows us to store that value in a variable

def add(a, b):
    x = a+b
    return x
sum1 = add(4,6)
sum2 =add(1,4)
sum3 = sum1+sum2
    #storing these return values in variables allows us to use the results of our functions
    #functions can return different date types
    #eamples: strings, numbers, lists , tuples, dictionaries and even functions

#RETURN ALSO MEANS EXIT & PRINT STATEMENTS FOR DEBUGGING
    #saving values: 
        # when you ptrint something with print(), it doesnt have any effect on your program, its mainly used to debug
        #a return statement may pass a value back to the outer scope after its done running for the program to use
    #exiting the function:
        #reaching a 'return' statement always means 'EXIT THIS FUNCTION NOW', any remaining code does not run

def full_name(name,name1):
    return name,name1

sum_name = full_name('eddie', 'aikau')
print(sum_name)

my_name=full_name('lazaro', 'alvarez')
print(my_name)