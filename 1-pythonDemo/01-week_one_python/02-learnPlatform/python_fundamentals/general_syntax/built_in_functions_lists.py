#BUILT-IN PYTHON FUNCTIONS FOR SEQUENCES
    #think of a sequence as anything we can iterate over.
    #len(sequence)
my_list=[1,'zen','hi']
print(len(my_list))

#EXAMPLES:  
    #len(sequence) -- returns the length (number of items) in a sequence
    #max(sequence) -- returns the highest value in a sequence
    #min(sequence) -- returns the lowest value ina sequence
    #sorted(sequence) -- returns a sorted sequence

#LIST-SPECIFIC METHODS
    #for built-in list methods you use dot-notation
    #some_list.pop()
my_list =[1,5,2,8,4]
my_list.pop()
print(my_list)#prints [1,5,2,8]

#COMMONLY USED LIST METHODS
    #list.append(value) -- appends a value to the end of lsit
    #list.pop(index) -- removes a value at a given index. if no parameter is passed, it will remove the last value in the list
    #list.index(value) -- returns the index(position) of the given value if it exists in hter list and rasies an error if it does not
    #list.reverse() -- reverses the roder of the elements,in place
    #list.sort() -- sorts the tiems in order of least to greatest, or alphabetically for strings, in place