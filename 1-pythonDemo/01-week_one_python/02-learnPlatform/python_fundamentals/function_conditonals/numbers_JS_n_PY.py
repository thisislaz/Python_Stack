#TO CONVERT NUMBERS YOU MUST USE THE FOLLOWING:
"""num_to_dec = float(num)"""

#RANDOM NUMBER BETWEEN 2-5
"""import random
    rand_num = random.randint(2,5)
"""

#NUMEBRS IN PYTHON
"""
int - whole numbers positive or negative
flaot - decimal nubmers, positive or negative
complex - are a part of the real number system and are often referenced with the letter j
    example: 1 + 3j.
    If youre not sure if you need to use them, its safe to say you can ignore this data type 
"""
#if youre unsure use the type() function
print(type(24)) #int
print(type(3.9)) #float
print(type(3j)) #complex

#CONVERSION
#all python objects have data type methods we can use to convert number types from one to another 
int_to_float = float(35) #the green words are the built ins and the blue are created
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

#RANDOM NUMBER
#python does not have a built inr andom nubmer generator, use the random module
import random
print(random.randint(2,5)) #provides a random number between 2 and 5
