#CONDITIONAL STATEMENTS 
    #keywords for condiotioanls in python are:
        #if, elif, else
x=20
if x> 50:
    print('bigger than 50')
else:
    print('smaller than 50')

x=55
if x>10:
    print('bigger than 10')#since this is the first true statemetn the condition has been met so it stop here
elif x>50:
    print('bigger than 50')
else:
    print('smaller than 10')

if x <10:
    print('smaller than 10')#is false nothing happens