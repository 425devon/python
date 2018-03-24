'''
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def fullName(arr):
    for d in arr:
        print d['first_name'], d['last_name']
fullName(students)
'''
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printNest(dic):
    count = 1
    charCount = 0
    print 'Students'
    for person in users['Students']:
        charCount = len(person['first_name']) + len(person['last_name'])
        print "{} - {} {} - {}".format(count, person['first_name'], person['last_name'], charCount)
        count += 1
    print 'Instructors'
    for person in users['Instructors']:
        charCount = len(person['first_name']) + len(person['last_name'])
        print "{} - {} {} - {}".format(count, person['first_name'], person['last_name'], charCount)
        count += 1
printNest(users) 