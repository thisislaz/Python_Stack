#MULTIPLE ARUGMENTS
    #if we want to capture multiple arguments into a single paramter we can place an asterisk before the name of the parameter after the "normal" paramtes
        #the asterisk is called a "splat" operator
def varargs(arg1, *args):
    print("Got ", arg1, " and ", args)
varargs("one") 			# output: Got one and ()
varargs("one", "two") 	# output: Got one and ('two',)
varargs("one", "two", "three","lazaro","bitch",23123) # output: Got one and ('two', 'three')
    #in this example the first argument "arg1" is assigned to the first method aprameter as usual.
    #however any and all remaining arguments passed in are in the "args" parameter, which appears to be a tuple (because its indicated by the () syntax)
    #because we prefixed the final parameter with an asterik(the splat operator), all the arguments that dont match a required parameter are packed into a single tuple
        #remember that a tuple is an iterable, just like a list
            #so to access them we can use a loop
def varargs(arg1, *args):
    for a in args:
    	print(a)
varargs("one", "two", "three","lazaro","bitch",23123) # output: two, three (on separate lines)

