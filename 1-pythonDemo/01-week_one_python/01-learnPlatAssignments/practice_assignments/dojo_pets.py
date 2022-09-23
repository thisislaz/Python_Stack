

class Ninja:
    all_my_ninjas = []
    def __init__(self,first_name,last_name,treats,pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        self.walk_pet = Pet(pet_qbi)
        Ninja.all_my_ninjas.append(self)

    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet_food.eat()
        return self

    def bathe(self):
        self.treats.noise()

    # @classmethod
    # def new_ninjas(cls):
    #     for nin in cls.all_my_ninjas:
    #         nin = Ninja()




class Pet:
    ninja_pets = []
    def __init__(self,type,tricks,health,energy):
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        Pet.ninja_pets.append(self)
    
    def sleep(self):
        self.energy +=25
        return self

    def eat(self):
        self.energy+=5
        self.health+=10
        return self

    def play(self):
        self.health+=5
        return self

    def noise(self):
        print(f"{self} lets out a roar!")
        return self

nin_laz = Ninja("lazaro","alvarez","milk bones","science diet","dog")
pet_qbi = Pet("dog","roll-over", 50,100)
Ninja.walk()
