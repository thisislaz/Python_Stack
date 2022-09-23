#user1.enroll()
#user1.display_info()
#user1.spend_points(50)
#user1.display_info()
#user2.enroll()
#user2.spend_points(80)
#user2.display_info()

#user1.display_info().enroll().spend_points(50).display_info()
#user2.enroll().spend_points(80).display_info()

#CHAINING
    #CHAINING is calling on the user1(self) once then attaching new method calls to the end of the previous ones
        #in order for this to work each method must return "self"
        #by returning self, eah method call will now be equal to the instance that called
    #for ex if user1.spend_points(50) returns its own instance(user1), then we can call one of that instances methods after that call
        #user1.spend_points(50).display_info()
class User:
    # .. constructor
    
    def display_info(self):
        # your code
    
    	# new return statement, returns this same object
        return self

    #the practice of having OOP return its own instance is pretty comon and is done in other proggramming languages
        #some languages use different variables however instead of "self" they use "this"
    #this only works with methods that do not need to return anything
    #if the method needs to return something other than self, it is not possibloe to chain the method
    