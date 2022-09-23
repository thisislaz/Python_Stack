#LOOPS

    #for loops with range()
    # rasnge() function can have between 1 and 3 arguments and creates a sequence of integers called a range object

#THREE WAYS TO USE RANGE()
    #only one argument
for i in range(5):#stops at 5 but does not include it
    print(i)#prints 0 1 2 3 4 vertically

    #two arguments
for i in range(2,7):#starts at 2 and stops at 7
    print(i)#prints 2 3 4 5 6 vertically

    #three arguments
for i in range(2,16,3):#starts at 2, stops at 16 but does not count it, increases by 3
    print(i)#prints 2 5 8 11 14 vertically

    #if you ever need to increment other than +1 you will need all three arguments
for x in range(0,10,2):
    print(x)#prints 0 2 4 6 8 vertically
for x in range(5,1,-3):
    print(x)#prints 5 2 