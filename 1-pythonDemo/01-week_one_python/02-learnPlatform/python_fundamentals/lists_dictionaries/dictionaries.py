#DICTONARIES
    #a dictionary is another mutable sequence type that can store any number of python objects
    #they consists of pairs(called items) of keys and their given values
    #this is the general summary of the characteristics of a python dict
        #a dictionary is an unordered collection of objects
        #values are accessed using a key(typically a string)
        #a dictionary can shrink or grow as needed
        #the contents of dictionaires can be modified
        #dictonaries can be nested
        #sequence operations such as slice cannot be used with dictionaries
    
#KEYS VS INDEXES
    #dictionaires use keys instead of indexes
    #Keys -	                                                                                                                Indexes
    #Keys are typically strings 	                                                                                Indexes are always integers.
    #Keys are not in any sort of order, as dictionary values are NOT stored sequentially in memory. 	        Indexes are ordered (least to greatest) as list and                                                                                                         tuple values are stored sequentially in memory.
    #Dictionaries ONLY have keys.	                                                                            Dictionaries DO NOT have indexes.

#CREATING DICTIONAIRES
    #dictionaires are enclosed by curly brackets {}
person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
capitals = {} #creates an empty dict

    #generally you will only use strings for the keys but can have any data typoe for the value

#ADDING NEW KEY-VALUE PAIRS
    #dictionaries dont have the .append method.
    #you can add new vlaues by setting a new key like with variables
    #literal notattion
person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
    #we created two dictionaries above in teo different ways
        #by using literal notation. the key-value pairs are enclosed by brackets, separated by commas. 
            #first value of a pair is a "key" nwhich is followed by a : and a "value"
            #the "first" string is a key and "ada" string is a value
        #by creating an empty dictionary and adding some values, 
            #the keys are inside the square brackets
            #the values are located on the right side of the assignment

#LIST SYNTAX
    #my_list[0]=4

#DICTIONARY SYNTAX
    #my_dict['some_string']=some_value

    #While the syntax for adding and changing values is similar to assigning values in a list, remember dictionaries do not use index numbers at all, instead you'll (almost always) see a string there, or some variable that resolves to a string:
