def check_num(num):
    new_list=[]
    for i in range(num,-1,-1):
        new_list.append(i)
    return(new_list)

print(check_num(5))

def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))

def values_greater_than_sec(list):
    if len(list)<2:
        return False
    new_list = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
    return new_list

print(values_greater_than_sec([5,2,3,2,1,4]))
print(values_greater_than_sec([3]))

def length_and_value(size,v):
    new_list=[]
    for i in range(0, size):
        new_list.append(v)

    return new_list

print(length_and_value)