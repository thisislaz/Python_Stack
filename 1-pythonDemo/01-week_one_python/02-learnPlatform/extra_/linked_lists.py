#LINKED LISTS

#ARRAYS 
    #arrays keep track of multiple values and are optimized for random access.
        #meaing we can access the values in the array by index numbers
            #myArray[3]
    #they are a good choice for when we need to keep values in a specific order or randomly access a given value somwhere in the middle.
        #this is possbile because arrays take up an entire set of consective cells in memory
        #not as strong when we have to insert or remove from the middle
    #LINKED LISTS are another data structure that stores values in sequential order
        #it is more optimized for quick insertion and deletion.
    #example: weve got an array of strings and we want to keep it alphabetical
#Alic,Chad,Debra,Eric,Fred
    #if we add Ben to our lsit; his name needs to be between alice and chad
    #we could say shift but that is an expensive operation
        #it means we have to alter potentially every element in the array just to add one item

#LINKED LISTS
    #linked lists instead of storing all values consecutively in memory, each element in the collection holds not only it value, but also a link to the element next to it
        #by using "nodes" we can store both of these pieces of data in one variable
    
#WHAT IS A NODE?
    #a "node" is a class that has two attributes:
        #value - the actual value to be stored (alice,ben, chad)
        #next - a link to the node next to it in the list.
            #for a computer this is a reference to or memory address of that node.
            #for developers this is a variable name that "points" to  another node.
            #if there isnt anthing next to it "next" can be set to "none"
class SLNode:
 def __init__(self, value):
  self.value = value
  self.next = None

#HOW TO GET FROM A NODE TO A LIST?
    #we have containers, or "nodes", for each element in our list, we now need a way to actually manage them.
    #as long as we know the first node we can get to every other node by starting at the front and moving to neighboring node as long as there is one
    #the following is the first node referred to as the "head" of the list
        #when we first create a lsit, it willl be empty
class SList:
    def __init__(self):
    	self.head = None
    
    #lets make an instance of our list:
my_list = SList()
    #this is the same concept as when we made User and BankAccount class; we are jsut doing it to represent a data structure called "singly linked list"

