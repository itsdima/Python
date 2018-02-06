info = {"name": "Eric", "age": "22", "country": "Moldova", "language": "Java"}
def printinfo():
	for key, data in info.iteritems():
		print "My name is", info.get("name")
		print "I am", info.get("age"), "years old"
		print "I was born in", info.get("country")
		print "My favorite coding language is", info.get("language")
		break
printinfo()