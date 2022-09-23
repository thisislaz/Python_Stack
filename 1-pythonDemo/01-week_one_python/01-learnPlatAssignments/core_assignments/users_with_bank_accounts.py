class BankAccount:
    total_accounts = []
    balance = 0
    int_rate = 2.5

    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.total_accounts.append(self)

    def display_account_info(self):
        print(f"Balance: ${self.balance} Intrest Rate: {self.int_rate}%")
        # print("=============")
        return self

    def desposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        #coudlve also done:
            if(self.balance - amount) >=0:
                self.balance -= amount
            else:
                print("Insufficient funds: Charging a $5 fee")
                self.balance -= 5
            return self
        #line 26 is saying: if True(is this true?); then execute line 28
        # if BankAccount.allow_withdraw(self.balance,amount):
        #     self.balance -= amount
        # else:
        #     print("Insufficient funds: Charging a $5 fee")
        #     self.balance -= 5
        # return self
        
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
    # @staticmethod
    # def allow_withdraw(balance, amount):
    #     if (balance - amount) < 0:
    #         return False
    #     else:
    #         return True

# savings = BankAccount(8.5, 250)
# checking = BankAccount(12.25,0)
# savings.desposit(100).desposit(120).desposit(100).withdraw(400).yield_interest().display_account_info()
# checking.desposit(100).desposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(200).yield_interest().display_account_info()
# BankAccount.all_accounts()

class User:
    other_user = []
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.savings_account = BankAccount(int_rate=5, balance=0)
        self.checking_account = BankAccount(int_rate=1, balance=0)
        User.other_user.append(self)

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}" )
        print(f"Age: {self.age}")
        print(f"Rewards member: {self.is_rewards_member}")
        print(f"Gold Points: {self.gold_card_points}")
        return self

    def enroll(self):
        self.gold_card_points = 200
        if self.is_rewards_member == False:
            self.is_rewards_member = True
        elif self.is_rewards_member == True:
            print("User is already a member.")
        return self
    
    def spend_points(self, amount):
        self.gold_card_points -= amount
        if  self.gold_card_points < 0:
            print('You do not have enough points to spend!')
            self.gold_card_points += amount
        return self

    def make_deposit_checking(self, amount):
        self.checking_account.desposit(amount)
        return self

    def make_deposit_savings(self, amount):
        self.savings_account.desposit(amount)
        return self
    

    def make_withdraw_checking(self,amount):
        self.checking_account.withdraw(amount)
        return self
    
    def make_withdraw_savings(self,amount):
        self.savings_account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"{self.first_name}'s checking balance: {self.checking_account.balance}")
        print(f"{self.first_name}'s savings balance: {self.savings_account.balance}")

        return self
    
    @classmethod
    def all_user_accounts(cls):
        for user in cls.other_user:
            user.display_user_balance()

    def transfer_money_savings(self,amount,other_user):
        if self.savings_account.balance > 0:
            self.make_withdraw_savings(amount)
            other_user.make_deposit_savings(amount) 
            return self
        else:
            self.savings_account.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            return self
    
    def transfer_money_checking(self,amount,other_user):
        if self.checking_account.balance > 0:
            self.make_withdraw_checking(amount) 
            other_user.make_deposit_checking(amount) 
            return self
        else:
            self.checking_account.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            return self



user_lazaro = User('lazaro', 'alvarez', '123email@email.com', 30)
user_karina = User('karina','khan','hasthree@email.com',29)
user_diplo = User('diplo','khan','businessdog@email.com',53)
user_qbi = User('qbi','alvarez','barista@email.com',12)


user_karina.make_deposit_checking(2500).make_deposit_savings(2000).transfer_money_checking(400,user_diplo).transfer_money_savings(200,user_lazaro).display_user_balance()
user_diplo.transfer_money_checking(100,user_qbi).transfer_money_savings(50,user_qbi).display_user_balance()
print('========')
User.all_user_accounts()