#ASSCIATION BETWEEN CLASSES
    #since we have a user class and abnkacounts class; wthere is an associtaiotn between these two classes
        #instead of keeping track of a balance directly in the User class, we'll encapsulate all the bank account information and associate a user with a specific instance of a BankAccount
    #assuming that each user has just one account that starts with a $0 balance and an int rate of %2
        #this means that the User class, instead od directly having a balance attribute, will actuallyy have an attribute of type BankAccount.
        #to establish this relationship, we can update our User's "__init__" method to something liek this:
            #removing the "account_balance" attribute and adding an account attirbute:
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line
    #the BankAccount class should be in the ame as the USer class, so the reference to it is recognized.
    #modularization is used if you need to have the 2 classes in separate files
    #we interact with this new attribute just as we do with previuous attributes
        #the only difference is that have personally dfined the functionality of this class!
    #we know the attributes and methods avaiable to the "account" attribute by looking at our BankAccount class
class User:
    def example_method(self):
        # we can call the BankAccount instance's methods
        self.account.deposit(100)
        # or access its attributes
        print(self.account.balance)



