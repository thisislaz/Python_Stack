#DEFAULT PARAMETERS & NAMED ARGUMENTS
    
#DEFAULT PARAMTERS
    #if we want to allow some of the parameters to be optional to the caller of the function we can set defaults

    #set defaults when declaring parameters
from ntpath import realpath


def be_cheerful(name='', repeat=2):
    print(f"good morning {name}\n" *repeat)
be_cheerful()#output: good morning (repeated on 2 lines)
be_cheerful('tim')#outputs good morning tim(reapted on 2 lines)
be_cheerful(name='john')#outputs good morning john(reapted on 2 lines)
be_cheerful(repeat=6)#outputs good morning (repeated on 6 lines)
be_cheerful(name='lazaro', repeat=69)#outpuits good morning lazaro(repeated on 69 lines)
    #argument order does not matter if we are explicit when sending in out arguments
be_cheerful(repeat=3, name='kori')#outputs good morning kori(repeated 3 times)