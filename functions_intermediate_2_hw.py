#A function can have multiple return statements. When any of them is executed, the function terminates.

x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)
    
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name']='Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['z']=30
print(z)


def iterateDictionary(students):
    for x in students:
        print('first_name', '-', x['first_name'], ',' 'last_name', '-', x['last_name'])
            

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students)


def iterateDictionary2(key_name, students):
    for x in students:
        print(x[key_name])
        

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


iterateDictionary2('first_name', students)


def iterateDictionary2(key_name, students):
    for x in students:
        print(x[key_name])
        

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


iterateDictionary2('last_name', students)


def printInfo(diction):
    for x in diction:
        print(len(diction[x]))
        print(x)
        for y in range (len(diction[x])):
                        print(diction[x][y])
            
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)

    
    


