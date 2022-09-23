drawers = ['documents', 'envelopes', 'pens']

    #the following accesess the drawer with index of 0 and prints value
print(drawers[0]) #prints documents
    #access the drawer with index 1 and print
print(drawers[1])#prints envelops
    #access the drawer with index 2 and print
print(drawers[2])#prints pens

    #replace 'documents' with 'roaches'
drawers[0] = 'roaches'
print(drawers) #prints: ['roaches', 'envelopes', 'pens']
    
    #stores the value 'roaches' in a temporary variable
top_contents = drawers[0]

    #replaces the vlaue at index 1
    #with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers)#prints: ['roaches', 'roaches', 'pens']

#LEFT-HAND-SIDE VS RIGHT-HAND-SIDE
    #whenever an indexed value in a list is ont eh right-hand side of the =, 'the assignment operator', the interperter has to fetch the raw value from memory
    #the left hand is indicating the location in memory only

#APPENDING VALUES TO A LIST
    #example to manipulate lists
    #some_list.append(some_value) --> only one value can be given at a time
    #the following appends a new item onthe the end of given list
nums = [1,2,3,4,5]
nums.append(99)
print(nums)#prints: [1, 2, 3, 4, 5, 99]

#SLICING
    #this returns a copy of some portion of a list
    #uses a copy of the list so you dont have to change the origianl
    #only use a portion of a list
    #the starting and ending index are separated by the ":" character
words = ['start','going','till','the','end']
    #sub-ranges(portions) of the list
print(words[1:])#prints: ['going', 'till', 'the', 'end']
print(words[:4])#prints: ['start', 'going', 'till', 'the']
print(words[2:4])#prints: ['till', 'the']