#FOUR PILLARS OF OOP
    #OOP is often used for web devlopment because its great for efficientcy and to reduce code length.

#BENEFITS OF USING OOP
    #Implements D.R.Y (Dont repeat yourself) code
    #Makes our application scalable
    #Makes our code reuseable
    #Makes our applications easily maintainable

#ENCAPSULATION  
    #the idea that we cna group code together into objects
    #uses classes or "coding blueprints" to define what our objects are and how they behave
    #we encapsulate attributes and methods in our class
    #ex:
class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")

#INHERITANCE
    #is the idea that we pass along attributes and methods from one class into a "sub-class" or child class and not have to rewrite the code to make it work
    #child classes can be more specific versons of their parents
    #key work "super" must be used to call methods
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")

#POLYMORPHISM
    #means "many forms" 
        #the idea in OOP is that a child class can have a different version of a method than the parent class
        #in our examples cappuccinoM has a clean method and so does coffeeM
        #depending on the class the clean method will do different things tho
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")
    def clean(self):
        print("Cleaning the froth!")

#ABSTRACTION
    #is an extension of "encapsulation", and we can hide attributes or methods that a barista doesnt need to know about, like coffeeM
    #that way the barista can make a cup of coffee in s simpler manner
class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def make_coffee(self, beans):
        self.cafe.brew_now(beans)





