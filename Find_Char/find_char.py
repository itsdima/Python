def find(list1, char):
	newlist =[]
	for idx in range(0, len(list1)):
		if list1[idx].find(char) != -1:
			newlist.append(list1[idx])
	if len(newlist) == 0:
		print "No matches found"
	else:
		print newlist

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
find(word_list, char)