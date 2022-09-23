#KEY-VALUE PAIR DATA STRUCTURES

#COMMON FORMAT FOR DATA-INTERCHANGE
    #key-value structures are oftern used for data coming from other sources, even from ecternal programs written in different languages, typically in form of JSON through an API, which can be parsed by Python into dictionaires.

#COMPARING DICTIONAIRES TO OOP CLASSES
    #similiarities    
        #dictionaires:
            #have unique keys for stored values
            #have access to many pieces of data through a single dictionary, using a key
        #OOP class:
            #have unique attribute names for stored values
            #have access to many attribute values through a single object instance using an attribute name
    #differences, limitations and advantages of each?
        #dictionaries:
            #can add new key-value pairs to an existing dictionary.
                #this is flexible, but doesnt suit data that should be uniform
            #can store functions, but does not inherently share these functions with other dictionaries
        #OOP classes:
            #generally cannot add new attributes to an existing object instance.
                #keeps data uniform, but has little capacity for non-uniform data
            #a class can have instance methods that are shared across all instances

#MAKING OBJECT INSTANCES FROM DICTIONARY DATA

    #this is a dictionary

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward",
    "team": "Brooklyn Nets"
}

    #if you were receiving data from an external source like a data base, and wanted to turn this dictionary into a "player" object
        #youd write your class like this:
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
    #now that the class is defined, take your dictionary info to make a player instance
    #Pass in all the values from the dictionary by their keys
player_kevin = Player(
    kevin["name"], 
    kevin["age"], 
    kevin["position"], 
    kevin["team"]
)
print(player_kevin.position) # prints small forward

#OTHER FACTS ABOUT DICTIONAIRES
    
#THEYRE FAST
    #almost every language has a built-in key-value pair data structure.
    #they are widely used, extremely powerful and considered fundamental for one primary reason:
        #they provide constant-time lookup, insertion and deletion on average
