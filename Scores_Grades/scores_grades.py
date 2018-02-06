def scores():
	print "Scores and Grades"
	import random
	for i in range(1, 11):
		score = random.randint(60, 100)
		if score >=60 and score <70:
			print "Score:", str(score)+";", "your grade is D"
		elif score >=70 and score <80:
			print "Score:", str(score)+";", "your grade is C"
		elif score >=80 and score <90:
			print "Score:", str(score)+";", "your grade is B"
		elif score >=90 and score <100:
			print "Score:", str(score)+";", "your grade is A"
		elif score >99:
			print "score:", str(score)+";", "A+! You're a ROCKSTAR"
	print "End of the program. Bye!"
scores()

