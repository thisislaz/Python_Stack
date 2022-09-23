#CLASSES    
    #blueprints of objects in object oriented programming
    #whenever we decalre a vairable, we creating an "instance" of a class
        #ex: x = [1,2,3], x is an "instance" of a list. 
    #an "instance" is an object that followd the pattern defined by its class
    #for a bank acc "user class" we would need diferent information compare to a "user class" for a social media acc
    #instead of allowing a user to define their own properties, we set a standard for what a user should have on our website
        #this ensures consistent creation of User instances
class User:
    pass #this is filled later

michael = User()#this is how we create a new instance of User class
anna = User()#this is how we create a new instance of User class
    #ATTRIBUTES: characteristics shared by all instances of the class type
    #METHODS: actiond that an object can perform. 
        #ex: a user in a bank app may need to be able to calcualte age based on the users birthday or open a new bank account associtated with that user

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
                              