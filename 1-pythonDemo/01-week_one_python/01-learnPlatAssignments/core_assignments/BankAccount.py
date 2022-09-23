class BankAccount:
    total_accounts = []
    
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.total_accounts.append(self)

    def display_account_info(self):
        print(f"Balance: ${self.balance} Intrest Rate: {self.int_rate}%")
        print("=============")
        return self

    def desposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        #coudlve also done:
            #if(self.balance - amount) >=0:
                #self.balance -= amount
            #else:
                #print("Insufficient funds: Charging a $5 fee")
                #self.balance -= 5
            #return self
        #line 26 is saying: if True(is this true?); then execute line 28
        if BankAccount.allow_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
        
    def yield_interest(self):
        #could have also done:
            #if self.balance > 0:
                #self.balance += (self.balance * self.int_rate)
        #the above only works if not giving percentages
        #the way i did it requires percentages as input
        if self.balance > 0:
            self.balance += self.balance*(self.int_rate/100)
        return self
    #creating a loop inorder to loop thrut he class attribute(total_accounts)
    #have to use the display_account_info() since we have already created it
    @classmethod
    def all_accounts(cls):
        for account in cls.total_accounts:
            account.display_account_info()
    
    #have to include this inorder to have math avaliable to our class
    @staticmethod
    def allow_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

savings = BankAccount(8.5, 250)
checking = BankAccount(12.25,0)
savings.desposit(100).desposit(120).desposit(100).withdraw(400).yield_interest().display_account_info()
checking.desposit(100).desposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(200).yield_interest().display_account_info()
BankAccount.all_accounts()