# #DEBUGGING IN PYTHON
#     #it is important to understand what is happening while you run your code
#     #try to debugg this:
# def multiply(num_list, num):#dont go insde the function until the function is called
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)#now our function executes what is a function call equal to?
# print(b)#and the resulting value is printed

#      #heres what happened in order:
#         #1. decalre a function
#         #2. instantiate a variable whose value is a list containing integers
#         #3. print the output of that function by calling it after a print statement

# def multiply(num_list, num):#test by adding print at the begining of the function
#     print(num_list, num)
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)

# def multiply(num_list,num):
#     print(num_list, num)
#     for x in num_list:
#         print(x)#lets confirm we are looping by printing x
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)

# def multiply(num_list,num):
#     print(num_list, num) # output should be [2,4,10,16] 5
#     for x in num_list:
#         print(x)
#         x *= num
#         print(x)#lets check ii were successfully changing our x value
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)

def multiply(num_list,num):
    print(num_list, num) # output should be [2,4,10,16] 5
    for x in num_list:
        print(x)
        x *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)

def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)