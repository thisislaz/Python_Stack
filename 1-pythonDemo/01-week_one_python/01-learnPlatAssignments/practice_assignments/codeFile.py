num1 = 42#variable declaration
num2 = 2.3#variable decalartion
boolean = True#primitive data type
string = 'Hello World'#variable declaration,
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#list, initializing
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#dictionary, initializing 
fruit = ('blueberry', 'strawberry', 'banana')#variable declaration, group of strings
print(type(fruit))#log statement and type check
print(pizza_toppings[1])#log statement, list access value
pizza_toppings.append('Mushrooms')#list adding value
print(person['name'])#log statement, dictionary access value
person['name'] = 'George'#dictionary change value
person['eye_color'] = 'blue'#dictionary add value and key
print(fruit[2])#log statement, string

if num1 > 45:#conditional
    print("It's greater")#skips
else:
    print("It's lower")#logs statement

if len(string) < 5:#condiontional
    print("It's a short word!")#skips
elif len(string) > 15:
    print("It's a long word!")#skips
else:
    print("Just right!")#logs statement

for x in range(5):#for loop,
    print(x)
for x in range(2,5):#for loop
    print(x)
for x in range(2,10,3):#for loop
    print(x)
x = 0#variable declaration
while(x < 5):#while loop
    print(x)
    x += 1

pizza_toppings.pop()#list delete value
pizza_toppings.pop(1)#list delete value by skipping 1 

print(person)#log statement
person.pop('eye_color')#dictionary remove key
print(person)#log statement

for topping in pizza_toppings:#loops thru pizza topping list
    if topping == 'Pepperoni':#conditional
        continue#skips value that is pepperoni
    print('After 1st if statement')#logs statement between if statements
    if topping == 'Olives':#conditional
        break#force stops loop

def print_hello_ten_times():#declares function
    for num in range(10):#for looop
        print('Hello')#log statment

print_hello_ten_times()#calls function

def print_hello_x_times(x):#creates parameter in function
    for num in range(x):#for loop that uses new parameter
        print('Hello')#log statement

print_hello_x_times(4)#provides value into parameter and calls function

def print_hello_x_or_ten_times(x = 10):#hardsets value for parameter
    for num in range(x):#for loop
        print('Hello')#log statement

print_hello_x_or_ten_times()#calls new function with x=10
print_hello_x_or_ten_times(4)#calls function and provides parameter


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)