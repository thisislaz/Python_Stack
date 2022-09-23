#NESTED DICTIONAIRES AND LISTS

#NESTING
    #nesting is allowed in dictionaires
    #dictionaires can contain lists and tuples as well was other dictionaries
    #on the flip lsits can also contain dictionaires

    # List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
    # Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}

#ACCESSING VALUES IN NESTED DICTIONAIRES
    #to access a value in a nested data structure take a look at how you would access the first users last name
print(users)
print(users[0]['last'])
print(users[1])
    #first "user[0]" is the whole user dictionary store at index 0
    #next find the value stored at the key "last" where we finally get the raw data "lovelace"
print(resume_data["skills"][1])
print(users[2]["first"])
    #lists are inside of []
    #dictionaries are inside of {}