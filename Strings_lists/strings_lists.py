#Find and Replace a word in string
words=  "it's thanksgiving day. It's my birthday, too!"
print words.find("day")
print words.replace("day","month")
#Min and Max values in array
x = [2,54,-2,7,12,98,"world"]
print max(x)
print min(x)
#First and last values in array, new list with the first and last values
x= ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x) -1]
newList= [x[0],x[len(x)-1]]
print newList
#New list, sort list, split list in half, push the first have of the list to possition 0 of the second half
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
half1 = x[0:len(x) /2]
print half1
half2 = x[len(x)/2:]
print half2
half2.insert(0, half1)
print half2

