#CHANGING OR UPDATING VALUES
    #each key in a dictionary must be unique
    #if you make an assignment using an existing key as the index, the old value will be changed for the new one
person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
    # Adds a new key value pair for email to person
person["email"] = "alovelace@codingdojo.com"
        
    # Changes person's "last" value to "Bobada"
person["last"] = "Bobada"
print(person)
    #adding a new value is the same syntax as updating a value

#TESTING FOR EXISTING KEYS
    #you want to check if a key already exists in teh dictionary to know whether to add an initail value or replace an existing one
    #if "some_key" in "my_dictionary":
        # update the value
    #this will also work with the "not" logical operator
if "email" not in person:
    person["email"] = "newemail@email.com"
else:
    print("Would you like to replace your existing email?")

#ACCESSING VALUES
    #to access the vlaues of a dictionary, you can use familiar square brackets along with key to obtain its value
# print(person["first_name"])
# full_name = person["first_name"] + " " + person["last_name"]

#REMOVING VALUES
    #there are two ways to remove a key:value from a dictionary
#value_removed = capitals.pop('svk') 
    # will remove the key 'svk' and return it's value
#del capitals['dnk'] 
    # will delete the key, and not return anything

#MULTI-LINE SYNTAX TOO!
    #you can write any dictionary's key-value pairs on multiple lines to make it easier to read, which is very useful for larger dictionaires.
#person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
    #the above can also be written like this:
#person = {
    #"first": "Ada", 
    #"last": "Lovelace", 
    #"age": 42, 
    #"is_organ_donor": True
#}

#COMMON BUILT-IN FUNCTIONS AND METHODS
    #python includes teh following standalone funciotns for dictionaries:
        #len()-give the total length of the dictionary
        #str()-produces a string representation of a dictionary
        #type()-returns the type of the passed variable.if passed variable is a dictionary, it iwll then return a dict type
    #these are very useful python dictionary "methods"
        #clear()-removes all elements from the dictionary
        #.get(key, default=none)-a safe way to get a value, if the key might not exist. returns the value for the specified key or "none"(or a value you specify) if the key is not in the dictionary
        #.update(pairs_to_update)- add and update multiple key-value pairs at once,l by passing in another dictionary of the pairs to update and add

