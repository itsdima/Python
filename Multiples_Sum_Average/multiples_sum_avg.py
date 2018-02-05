#Multiples- print all odd numbers from 1-1000 
for count in range(1,1001):
	if count % 2 != 0:
		print count

#Multiples- print all multiples of 5 from 5 to 1,000,000
for count in range(5, 1000001):
	if count % 5 == 0:
		print count
#Sum list- print sum of all values in a list
a = [1,2,5,10,255,3]
sum = 0
for idx in range(0, len(a)):
	sum += a[idx]
print sum
#Average list- print avg of values in the list
a = [1,2,5,10,255,3]
avg = sum(a)/len(a)
print avg
