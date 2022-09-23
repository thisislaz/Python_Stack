class User:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greeting(self):#adding the greeting method
        print(f"hello my name is {self.first_name}. and im tired")
    
    def tired(self):#adding the tired method
        print(f'i mr.{self.last_name} am tire af because i am {self.age} years old now')

lazaro = User('lazaro','alvarez', 30)
lazaro.greeting()
lazaro.tired()

#METHODS
    #"methods" are jsut functions that belong to a class. 
        #this means that wecant call them independently as we have called functions previously; rather methods must be called from an instance of a class
    #to get custom grettings for users, like :"hello my name is lazaro. and im tired", we want to be able to call the method "from the user instance" using dot-notation because each user has a differnt name
    #the calls look something like this:
lazaro.greeting()
    #inorder to call this method it must exist.
        #new methods have been added in lines 7 and 10
    #dont forget the first parameterof every method must be "self"
    #methods also have access to the class's attirbutes
karina = User('karina', 'khan', 29)
karina.greeting()
karina.tired()

#SELF
    #the "self" parameter includes all the information about the individual object that has called the method.
        #because we are calling on hte method "from the instance", this is known as "implicit passage of self"
    #when we can on a method from an instance, the memory address of that instance, along with all of its information(first_name,last_name, age), is passed in as self
    