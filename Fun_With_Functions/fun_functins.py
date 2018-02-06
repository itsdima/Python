# print each number 1-1000 and specify weather it is odd or even
def odd_even():
	for i in range(1, 2001):
		num = "Number is"
		odd = ""
		if i % 2 == 0:
			odd = "This number is even"
		else:
			odd = "This number is odd"
		print num, str(i)+".", odd
odd_even()
#multiply each value in a given list by the given number (5)
def multiply(a, by):
	for i in range(0, len(a)):
		a[i] = a[i] * by
	print a
a = [2,4,10,16]	
b = multiply(a, 5)
print b