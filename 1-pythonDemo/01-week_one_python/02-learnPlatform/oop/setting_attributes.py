#SETTING ATTRIBUTES
class Shoe:                                             #CLASS - shoe
    def __init__(self):                                 #ATTRIBUTES
        self.brand = "adidas"                               #brand
        self.type = "tennis shoe"                           #wear/activity type
        self.price = 45.99                                  #price
        self.in_stock = True                                #stock status

    def rebrand(self,new_brand):                        #METHODS
        self.brand = new_brand                              #sold out(changes the sticj staus to "false")
    def sold_out(self):                                     #rebrand (updates the shoe brand name)
        self.in_stock = False                               #on sale(decreases the price by a percentage)
    def on_sale(self, percent):
        self.price = self.price *(1- percent)   
#INSTANCE ATTRIBUTES
    #"instance attributes" are defined in the constructor,the "__inti__" method, wich is called when a new object is instantiated, in this case, when a new type of shoes is added in invetory                    
class Shoe:
    def __init__(self):
        self.brand = "vans"
        self.type = "classic sk8-hi"
        self.price = 69.99
        self.in_stock = True
    #the first parameter of an instance method within a class will always be "self" and the instance attributes are also indicated as "self"
    #"self" is a reference to the instance, not the class, in this case this particualr pair of shoes, not the generic "Shoe" class
    #now we can create instances of "Shoe" outside the scope of the class definition
skater_shoe = Shoe()
dress_show = Shoe()
    #accessing the instance's attributes
print(skater_shoe.type)#prints classic sk8-hi
print(dress_show.type)#prints classic sk8-hi
    #we can also set the values for our instances attirbutes
skater_shoe.type = "low-top trainers"
print(skater_shoe.type)#now value has changed to low-top trainers
dress_show.type = "ballet flats"
print(dress_show.type)#now it has been changed to "ballet flats"

#PASSING IN ARGUMENTS
    #we want all the shoes to have a brand,type, price, and status, but we dont want all of our shoes to have the same info upon creation
        #how will we know what the type should be?
    #now we pass arguments into the "__init__" method to specify a shoes instance attributes
    #in this example even tho we have 4 instance attributese we only need 3 inputs
    #when a new Shoe is entered well require: brand, type and price
        #lets adjsut our code to allow arguments to be passed in upon instantiation
class Shoe:
    def __init__(self,brand,shoe_type,price):
        #here we now have 4 parameters inclduing self!
        self.brand = brand
        self.type = shoe_type
        self.price = price
        #the status is set to True by default
        self.in_stock = True
skater_shoe = Shoe('vans','low-top trainers', 59.99)
dress_show = Shoe('jack & jill bootery', 'ballet flats', 29.99)
print(skater_shoe.type)#still prints low-top trainers
print(dress_show.type)#still prints ballet flats