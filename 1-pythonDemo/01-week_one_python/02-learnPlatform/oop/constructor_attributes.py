#CONSTRUCTOR AND ATTIRBUTES

#THE CONSTRUCTOR
    #since we want all users to have the same pieces of info, its good to ahve a uniform way to always include that data whenver a  user is created
    #constrcutor is used for this: it is a function that contains instructions for making a new instance of a class, in the above scenerio: a new user
    # in Python the specail function "(__init__)" is the method used for this
    # when calledthis method will designate some space in memory to store the user, and then assign the first name, last name and age by executing the lines below 

class User: #decalre a class and give it name User
    def __init__(self):
        self.first_name = "ada"
        self.last_name = "loveface"
        self.age = 42
    #the term "method" is used to refer to functions that specifically "belong" to a class.
        #in other words: the functions that are defined inside the scope of a class definition

#MAKING INSTANCES
    #by defining the "User" class we've defined a new "data type" "User"
    #in the same way we can create different lists or dictionaries we can create and store many different users
    #you can use the syntax "Your_Class_Name" to create and then store a new instance of a class
        #in this case "User"; to make and save a new user in memory
            #this will still need a variable to store it in
    #for the most part youll crate your object instances "outside" the class definition; in the outer "global scope"

    #now ththat we have a class set up with a constructor (line 10), we can assign new variables to new users in the outer scope

user_ada = User()
print(user_ada.first_name)#prints ada
    #this example is jsut storing two strings and a anumbner together in the variable "user_ada"
        #this is similiar to how dictionaries store multiple pieces of data in one place.
        #they are stored as one data type "User"
        #they can be accessed with the dot-notation:"user_ada.first_name"

#INTRO TO SELF
    #"self" is a placeholder for future instances, future users, like a blank form
    #in the above ex the "user_ada = User()" is executed and the "__intit__" method is called
        #its like a patient handing in the clipboard to the receptionist
    #the "self" is referring to "user_ada"
    #if another variable is created "user_2 = User()", the constructor is called again but this time "self" variable inside the constructor will refer to "user_2"
        #like a different patient handing in their form
user_2 = User()
print(user_2.first_name)
    #everyone will have default names of ada atm since the class defaluts are as such
    