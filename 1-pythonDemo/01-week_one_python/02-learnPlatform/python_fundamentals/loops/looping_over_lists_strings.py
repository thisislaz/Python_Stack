#LOOPING OVER LISTS AND STRINGS

#FOR LOOPS THRU STRINGS
    #you can access each value of a string individually with loop
for x in 'hello':
    print(x)#prints h e l l o vertically

#FOR LOOPS THRU LISTS
    #for lists we can use the range function and send in the length of the list as the stopping value
    #if we are not interested in the index vlaues we can see the values in order we can jsut loop thru it
my_list = ['abc', 123, 'xyz']
for i in range(0, len(my_list)):
    print(i,my_list[i])#this prints the index  and the value inside it
                       #0 abc 1 123 2 xyz; vertically and the index alongside its value

for v in my_list:
    print(v)#only prints values in indexes

#WHILE LOOPS
    #another way of looping WHILE a certain conndition is true
for count in range(0,5):
    print(f'looping = {count}')#can also be written as: 
                               #print('looping =', count)
    #this is the while loop version of the above loop in lines 21
count = 0
while count <= 5:
    print('looping -', count)
    count +=1#this logs 5 tho; probably someone going too fast

    #th basic while loop syntax looks like this
    #while <expression>:
        #do something, including progress towards making the expression false.
        #otherwise itll be an infinite loop
    #if condition was somehow not meant but you want to do something regardless:
y=3
while y > 0:
    print(y)
    y = y - 1
else:
    print('final else statement')
    #the else is only executeed becasue the loop was able to finish
    #if the loop is returned or breaks, then the else will never be triggered

#LOOP CONTROL
    #control flow -- the cornerstone of most programming languages
    #loops,breaks, and continues are all a part of control flow

#BREAK
    #break -- exits the current loop prematurely, resuming execution at the first post-loop statement. used in both types of loops
for val in 'string':
    if val == 'i':
        break
    print(val)#prints s t r vertically. stops at i due to condition

#CONTINUE
    #continue immediately returns control to the beinging of the loop
    #it skips, or rejects all the remaining statements in thre current iteration of the loop and continues normal execution at the top of the loop
    #most useful for skipping certain iterations but want to loop to the end
for val in 'string':
    if val == "i":
        continue
    print(val)#prints s t r , skips 'i', n g vertically

y=3
while y > 0:
    print(y)
    y = y- 1
    if y == 0:
        break
else: #only excutes on a clean exit from thw while loop; without a break.
    print('final else statement')