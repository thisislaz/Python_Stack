#CLASS AND STATIC METHODS

#CLASS VS INSTANCE
    #we have now accustomed to desinating instance attirbutes inside the constructor using the "__init__" method
    #we can declare and set attirbutes that dont belong to a single instance but to the the class itself
    #normally when we create a method on a class we pass in "self" to the "instance" of the object

#CLASS ATTRIBUTES
    #"class attributes" are defined outside of any instance methods, and is shared among all instances of the class
class BankAccount:
    # Declaring a class attribute
    # Shared among all bank accounts
    bank_name = "First National Dojo"		
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    #class attributes are more flexible because we can change them on an instance or the entire class
    #changing them on an instance:
adriensAccount = BankAccount()
sadiesAccount = BankAccount()
adriensAccount.bank_name = "Dojo Credit Union"    
print(adriensAccount.bank_name)
    # output: Dojo Credit Union
print(sadiesAccount.bank_name)
    # output: First National Dojo
    #changing them on the entire class:
BankAccount.bank_name = "Bank of Dojo"
print(adriensAccount.bank_name)
    # output: Bank of Dojo
print(sadiesAccount.bank_name)
    # output: Bank of Dojo

#@CLASSMETHOD
    #class methods are defined with a decorator @classmethod
        #they belong to the class itself instead of the instance
        #instead of implicitly passing "self" into the method, we pass "cls"
    #ex of @classmethods:
class BankAccount:
    # class attributes
    bank_name = "First National Dojo"
    # new class attribute - a list of all the accounts!
    all_accounts = []
    
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum
    #its important to know that class methods have no access tot he instance attribute or any attribute that starts with "self"

#@STATICMETHOD
    #static methods are functions defined within the class with a decorator "@staticmethod"
    #they have NO access on "instance" or "class" attributes, so if we weed any existing values, they need to be passed in as arguments
    #if we wanted out BankAccount class to ahve a utility function to add or subtract we could implement "@staticmethod" on the class
class BankAccount:
    # ... __init__ goes here
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can withdraw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
    	if (balance - amount) < 0:
            return False
        else:
            return True




