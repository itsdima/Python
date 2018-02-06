#below is part 1 of the assignment 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def printnames():
	for i in range(0, 4):
		print students[i].get("first_name"), students[i].get("last_name")
printnames()
#Below is part 2 of the assignment
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
def printall():
	print "Students"
	for i in range(0, 4):
		# print users["Students"][i].get("first_name"), users["Students"][i].get("last_name")
		print (i+1), "-", users["Students"][i].get("first_name"), users["Students"][i].get("last_name"), "-", len(users["Students"][i].get("first_name"))+len(users["Students"][i].get("last_name"))
	print "Instructors"
	for x in range(0,2):
		print (x+1), "-", users["Instructors"][x].get("first_name"), users["Instructors"][x].get("last_name"), "-", len(users["Instructors"][x].get("first_name"))+len(users["Instructors"][x].get("last_name"))
printall()
