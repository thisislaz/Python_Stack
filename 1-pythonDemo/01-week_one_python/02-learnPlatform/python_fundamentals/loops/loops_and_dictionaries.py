#LOOPS AND DICTIONARIES

#FOR LOOPS THROUGH DICTIONAIRES
    #dictionaires are also iterable
    #when iterating thru a dictionary, the iterator is each key
my_dict = { "name": "Noelle", "language": "Python" }
for i in my_dict:
    print(i)
    #in order to get the "values":
my_dict = { "name": "Noelle", "language": "Python" }
for i in my_dict:
    print(my_dict[i])
    #more examples of methods to iterate thru dictionaires
capitals = {
    "Washington":"Olympia",
    "California":"Sacramento",
    "Idaho":"Boise",
    "Illinois":"Springfield",
    "Texas":"Austin",
    "Oklahoma":"Oklahoma City",
    "Virginia":"Richmond"
}
    # another way to iterate through the keys
for i in capitals.keys():
     print(i)
    # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
    
    #to iterate through the values
for val in capitals.values():
     print(val)
    # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
    
    #to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)
    # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

