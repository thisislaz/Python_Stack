#LISTS
    #same as arrays in javescript and other languages
    #created with [] where each value is seperated by a comma\
    #same characteristics as in js
ninjas = ['rozen', 'kb', 'oliver']
print(ninjas)
my_list = ['4',['list','in', 'a', 'list'], 987]
print(my_list) 
empty_list = []

    #you can combine and duplicate values fairly easy, by using the + and *
    #if you 'add' the lists it contains all the values of both arrays.
    #if you multiply it will copy call the vlaues of the lsit by that whole number and create a new list with the neew values
    #whichever of the two you do, it adds the value to the end of the list(array)
fruits = ['apple','banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)