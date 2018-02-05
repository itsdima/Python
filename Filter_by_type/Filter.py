#filter by type- function that tests the values for its type and prints a message about them
def typetest(val):
	if isinstance(val, int):
		if val >= 100:
			print "Thats a big number!"
		else:
			print "Thats a small number"
	if isinstance(val, str):
		if len(val) >= 50:
			print "Long sentence"
		else:
			print "short sentence"
	if isinstance(val, list):
		if len(val) >= 10:
			print "Big list"
		else:
			print "short list"

typetest("Rubber baby buggy bumpers")