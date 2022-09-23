# x = [ [5,2,3], [10,8,9] ] 
# z = [ {'x': 10, 'y': 20} ]
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# x[1][0] = 15
# students[0]['last_name'] = 'Bryant'
# sports_directory['soccer'][0] = 'Andres'
# z[0]['y'] = 30
# print(z[0])

# def iterate_dictionary(some_list):
#     for i in range(len(some_list)):
#         empty_str = ""
#         for key, val in some_list[i].items():
#             empty_str+= f"{key}-{val},"
#         print(f"{empty_str}")


def iterateDictionary(list):
    for student in list:
        # print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")
        for key in student:
            print(f"{key} - {student[key]}")


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterate_dictionary(students) 
iterateDictionary(students)

# def iterate_dictionary_two(key_name, some_lists):
#     for i in range(len(students)):
#         print(some_lists[i][key_name])

# iterate_dictionary_two('first_name',students)

# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def print_info(some_dict):  
#     print(f"{len(some_dict['locations'])} LOCATIONS")
#     for i in some_dict['locations']:
#         print(i)    
#     print(f"{len(some_dict['instructors'])} INSTRUCTORS")
#     for i in some_dict['instructors']:
#         print(i)
    
# print_info(dojo)