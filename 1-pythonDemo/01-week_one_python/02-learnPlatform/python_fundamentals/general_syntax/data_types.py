#boolean values - asseses the truth value of something. True or False
from hashlib import new
from turtle import numinput


is_hungry = True
has_freckles = False

#numbers are integers(whole numbers), floating point numbers(decimal numebrs) and complexx numbers
age = 35 #storing an int
weight= 160.57 #storing a float

#strings are literal text
name = 'joe blue'


#COMPOSITE TYPES

#TUPLES - a type of data that is immutable(cant be changed) and can hold a group of values. can contain mixed data types
#these are like CONST in js
dog = ('bruce', 'cocker spaniel', 29, False)
print(dog[0]) #output:bruce
# dog[1] = 'dachsund' #error: cannot be modified


#LISTS - type of data that is mutable and can hold a group of values. usually meant to store a collection of related data
#this are like ARRAYS in js
empty_list = []
ninjas = ['rozen', 'KB', 'oliver']
print(ninjas[2]) #output: oliver
ninjas[0] = 'francis'
ninjas.append('michael') #adds it to the end THIS IS .PUSH()
print(ninjas) # output:['francis', 'kb', 'oliver','michael']
ninjas.pop() #same as in js
print(ninjas)
ninjas.pop(1)
print(ninjas) #outout: ['francis','oliver'] i believe it just skipps 1

#DICTIONAIRES - a group of key-value pairs
#these are objects from js
empty_dict = {}
new_person = {'name':'john', 'age': 29, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'jack' #updates the value if key exists, adds a value-pair if it doesnt
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person['weight']
print(w)
y = new_person.pop('weight')
print(new_person)

#COMMON FUNCTIONS
#we can use a built in function to detemine what type of data a variable is by using TYPE():
print(type(2.63)) #class 'float'
print(type(new_person)) #class dictionary

#we can use the built in function LEN() to get the length of attirbutes that have lengths (lists, dictionaries,tuples,strings)
print(len(new_person)) #prints 4
print(len('coding dojo')) #prints 11; so it counts the spaces too