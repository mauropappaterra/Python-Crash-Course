# Python Crash Course
# dictionaries.py
# Created by Mauro José Pappaterra on 24 February 2017.

#Python Dictionaries are just like Java HashTables... but...

############################################ CREATE A DICTIONARY

dictionary = { 'key_1': 'value', 'key_2': 'v', 'key_3': 1 } # a collection of keys => values

print(dictionary) # prints all keys and values

contact_1 = { 'name': 'Joe', 'last name':'Rey', 'phone':'456-234-6789', 'dob': 1989 }
contact_2 = { 'name': 'Johnny', 'last name':'Bravo', 'phone':'478-394-1126', 'dob': 1994 }
contact_3 = { 'name': 'Patti', 'last name':'Smith', 'phone':'632-337-9254', 'dob': 1954 }

birthdays = { # another way to indent when defining a dictionary (++ syntactic sugar))
    'Ann' : 1992,
    'Luke' : 1999,
    'Thomas' : 1985,
    'Mary' : 1976,
    'Bobby' : 1954,
    'Edward' : 1989,
    'Sarah' : 1985,
    'Sophie' : 2000,
    'Andrew' : 1992,
}

print(birthdays)

############################################ RETRIEVE VALUES FROM DICTIONARY

print (contact_1['name'] + "'s " + contact_1['phone'])
print (contact_2['name'] + "'s " + contact_2['phone'])
print (contact_3['name'] + "'s " + contact_3['phone'])

############################################ ADD A NEW K
#
# EY-VALUE PAIR

date = {} # empty dictionary

date['day'] = '23' # add new key and value
date['month'] = 'February'
date['year'] = '2017'

print (date['day'] + "rd " + date['month'] + " " + date['year'])

############################################ MODIFY A DICTIONARY

print (contact_1['name'] + "'s " + contact_1['phone'])

contact_1['phone'] = '999-345-1212' # modify value stored in key by name

print (contact_1['name'] + "'s " + contact_1['phone'])

############################################ DELETE KEY FROM DICTIONARY

print(contact_1)

del contact_1['dob']

print(contact_1)

############################################ ITERATE DICTIONARY

for key, value in contact_1.items(): # using a for statement
    print("\nKey: " + key)
    print("Value: " + value)

for name in birthdays.keys(): # using a for statement and method .keys() for iterating keys
    print(name)

for name in sorted(birthdays.keys()): # iterating dictionarie's keys in alphabetical order
    print (name)

for dob in birthdays.values(): # using a for statement and method .values() for iterating values
    print(dob)

for dob in sorted(birthdays.values()): # iterating dictionarie's values in alphabetical order
    print(dob)

for dob in set (birthdays.values()): # using method set() for avoiding repeated values
    print(dob)

for key, value in birthdays.items(): # return dictionary key instead of the value
    if value == '1992':
        print (key) # will print all the keys with the value '1992'

############################################ NESTING

contacts = [contact_1,contact_2,contact_3] # a list of dictionaries

for contact in contacts:
    print (contact)

car = { # a dictionary of lists
    'make': ['BMW','Ferrari','Mustang','Lamborghini','Audi'],
    'color': ['red','white','blue'],
    'year': [range(1954,2017)]
}

for make in car['make']:
    print (make)

users = { # a dictionary of dictionaries

    'user0001' : {
        'username' : 'bobby_malone',
        'password' : 'california2017'
    },

    'user0002' : {
        'username' : 'marla_burns',
        'password' : 'SantaCruz1976!'
    },

    'user0003' : {
        'username' : 'junipero_sierra',
        'password' : 'mission4god1645'
    }

    #...
}

for user, user_info in sorted(users.items()):
    print ('\n' + user)
    print ('Username: ' + user_info['username'])
    print ('Password: ' + user_info['password'])

############################################ SORTING


dic_array = [
    {'name':'John', 'age':29},
    {'name':'Vivian', 'age':39},
    {'name':'Ally', 'age':39},
    {'name':'Manny', 'age':13},
    {'name':'Albert', 'age':76}
    ]

sorted(dic_array, key=lambda i: i['age']) # sort by age
sorted(dic_array, key=lambda i: (i['age'], i['name'])) # sort by age then name
sorted(dic_array, key=lambda i: (i['name'], i['age'])) # sort by name then age
sorted(dic_array, key=lambda i: i['age'], reverse=True) # sort by age descending
