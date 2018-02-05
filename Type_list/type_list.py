#type list- print message for each element in the list, base on that elements data type
def typelist(arr):
	numCount = 0
	strCount = 0
	sumTotal = 0
	strlist = "String: "
	for idx in range(0, len(arr)):
		if isinstance(arr[idx], int) or isinstance(arr[idx], float):
			numCount = 1 
			sumTotal += arr[idx]
		if isinstance(arr[idx], str):
			strCount = 1 
			strlist += arr[idx]
	if numCount + strCount == 2:
		print "The list you entered is a mixed type"
		print strlist
		print "sum:", sumTotal
	elif numCount == 1 and strCount == 0:
		print "The list you entered is an integer type"
		print "sum:", sumTotal
	elif numCount == 0 and strCount == 1:
		print "The list you entered is a string type"
		print strlist
	    
typelist(["magical","strings"])