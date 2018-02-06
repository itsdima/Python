def cointoss():
	print "Starting the program..."
	import random
	heads = 0
	tails = 0
	for i in range(1, 5001):
		chance = random.randint(1,2)
		if chance == 1:
			heads+=1
			print "Attempt #"+str(i), "Throwing a coin...", "It's heads", "... You had", heads, "head(s) so far and", tails, "tail(s) so far"
		elif chance == 2:
			tails+= 1
			print "Attempt #"+str(i), "Throwing a coin...", "It's tails", "... You had", heads, "head(s) so far and", tails, "tail(s) so far"
	print "Ending the program, thank you!"
cointoss()