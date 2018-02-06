def compare(str1, str2):
	if len(str1) != len(str2):
		print "The lists are not the same"
	elif len(str1) == len(str2):
		for idx in range(0, len(str1)):
			if str1[idx] != str2[idx]:
				print "The lists are not the same"
				return
		print "The lists are the same"
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compare(list_one,list_two)
