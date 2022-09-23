class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
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

        

user_lazaro = User('lazaro', 'alvarez', '123email@email.com', 30)
user_karina = User('karina','khan','hasthree@email.com',29)
user_diplo = User('diplo','khan','businessdog@email.com',53)
user_qbi = User('qbi','alvarez','barista@email.com',12)



user_lazaro.enroll().spend_points(50).display_info().enroll()
user_karina.enroll().spend_points(80).display_info()
user_diplo.display_info().spend_points(40)
user_qbi.display_info()







