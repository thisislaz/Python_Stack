#INHERITANCE
    #defining a new class based on another class
        #allows one class to take on the attributes and methods from another class with little additional code
        #this code reuse reslults in reduced redundancy and complexity
    #the derived classes(referred to as "child" or "sub class") can override or extend the functionality of base classes(parent or super classes)
    #if in BankAccount class we wanted to have both checking accounts and retirement accounts there would be a lot of thiings these two types of accounts have in coomon, but some attributes and methods would differ from the two
    #we could add an "account_type" 
        #then in each of our methods, we would have a series of conditional statements that would determine how the method would actually run
            #this gets clunky and hard to manage
        #an alternative would be to create two classes that would look like this
class CheckingAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
    	pass#
    def withdraw(self, amount):
    	pass#
    def write_check(self, amount):
    	pass#
    def display_account_info(self):
    	pass#

class RetirementAccount:
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    	self.is_roth = is_roth
    def deposit(self, amount):
    	pass# - assess tax if necessary
    def withdraw(self, amount):
    	pass# - assess penalty if necessary
    def display_account_info(self):
    	pass#
    
        #this may still feel repetitive
        #inheritance provides a blaance between the two
            #it allows to have a parent class that holds the attributes and methods that are common between the classes
            #in return the child class will only contain what is unique to that class
class CheckingAccount(BankAccount):
    pass    
class RetirementAccount(BankAccount):
    pass

        #with just the inclusion of the parent class in parentheses, both the checkingaccount and retirement account classes both have all the attributes and functionality of the parent class


#SUPER
    #this is what the retirementaccount __init__ method does and what the parent bankaccount class __init__ does
class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.is_roth = is_roth  

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    
    #to indicate we are trying to use the parents methods, we call on it with the keyword "super", then we can call on any of the parents methods
class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)	
        self.is_roth = is_roth	

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    #the first line in our retirementaccount __init__ method allows the parent to manage the setting of int_rate and balance
    #the only line that needs to be added is set to the "is_roth" attribute, since its unique to the retirementaccount class
    #add some logic to our withdraw method:
class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

class BankAccount:
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self
        
    #call on the parent to do the part of the code that is the same
class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self
    
class BankAccount:
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self







