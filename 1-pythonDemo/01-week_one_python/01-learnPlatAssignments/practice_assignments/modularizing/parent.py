local_val="magical unicorns"
def square(x):
    return x*x
class User:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        return "hello"

print(square(5))
user = User('anna')
print(user.name)
print(user.say_hello())
print(__name__)
if __name__ == "__main__":
    print('the file is being executed directly')
else:
    print("the file is being executed becasue it is imported by antoher file. the file is called:", __name__)