#STRING LITERALS
    #strings are sequence of characters enclosed inside qoutation marks
print('this is a string')

#CONCATENATING STRINGS AND VARS WITH THE INPUT FUNCTION
    #adding a comma after the string, followed by the variable, comma must be outside the quotes
    #ths print() function inserts a space between the elements sepereated by a comma
name = 'zen'
print('my name is', name)
    #the second way is by concatenating the contents into a new string with the help of +
name = 'zen'
print('my name is ' + name) #put space after before the closing quote so there is a space in the string
print('my name is '+ name, 5)
# print('my name is ' + name + 5) #this gives an error

#TYPE CASTING OR EXPLICIT TYPE CONVERSION
    # print('my name is ' + name + 5) #this gives an error 
print('hello, the following is a number that is added to this string '+ str(42))

    #receive a string inpout from a user that we want to treat as a number
total = 35
user_val = '26'
# total = total + user_val #error
total = total + int(user_val) #total = 61
print(total)

#STRING INTERPOLATION METHODS
    #F-STRINGS(LITERAL STRING INTERPOLATION)
    #place an f right before the opening quote. then within the string, place any variables within curly brackets
first_name = 'zen'
last_name = 'coder'
age = 27
print(f'my name is {first_name}{last_name} and i am {age} years old')

#STRING.FORMAT()
    #type out the full string, replacing any words that will get their values from variables with {}.
    #then call the format method on the string, passing in arguements in the order in which they should fill the {} placeholders
first_name = 'lazaro'
last_name = 'alvarez'
age = '29'
print('my name is {} {} and i am {} years old. '.format(first_name,last_name, age))
#this prints the following: my name is lazaro alvarez and i am 29 years old.
print('my name is {} {} and i am {} years old. '.format(age,first_name,last_name))
#this prints the following: my name is 29 lazaro and i am alvarez years old.

#%-FORMATTING
    # the % can also indicate a placeholder
        # %s is sued fors trings 
        # %d for numbers
        #a single % after the string separates the string to be interpolated from the values to be inserted into the string
hw = 'hello %s' % 'world'
py = 'i love python %d' % 3
print(hw,py) #prints i love python 3
name = 'zen'
age = 27
print('my name is %s and im %d' % (name,age))#with variables
#this prints:my name is zen and im 27

#BUILT-IN STRING METHODS

x = 'hello world'
print(x.title())#this prints 'hello world'


"""
string.upper(): returns a copy of the string with all the characters in uppercase.

string.lower(): returns a copy of the string with all the characters in lowercase.

string.count(substring): returns number of occurrences of substring in string.

string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.

string.find(substring): returns the index of the start of the first occurrence of substring within string.

string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include 
spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.

string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.

string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.

"""