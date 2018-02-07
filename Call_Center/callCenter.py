class Call(object):
	def __init__(self, unq, name, num, time, reason):
		self.unq = unq
		self.name = name
		self.num = num 
		self.time = time
		self.reason = reason
	def display(self):
		print self.unq, self.name, self.num, self.time, self.reason
call1 = Call("12", "eric", "333444555", "3:40", "cuz im pissed")
call2 = Call("13", "erik", "333444565", "3:38", "cuz im not pissed")
call3 = Call("14", "eri", "33344565", "3:42", "cuz")
call4 = Call("14", "eri", "3", "3:18", "works")

class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.size = 0
	def addCall(self, call):
		self.calls.append(call)
		self.size +=1
		return self
	def remove(self, call):
		self.calls.remove(call)
		self.size -=1
		return self
	def removebynum(self, bynum):
		for i in range(0, len(self.calls)):
			if self.calls[i].num == bynum:
				self.calls.remove(self.calls[i])
				self.size -= 1
				break
		return self
	def info(self):
		for i in range(0, len(self.calls)):
			print self.calls[i].name
			print self.calls[i].num
		print "Queue:", self.size
		return self
	def sort(self):
		self.calls.sort(key = lambda x: x.time)
		return self


CC = CallCenter()
CC.addCall(call1).addCall(call2).addCall(call4).addCall(call3).sort().info().removebynum("33344565").removebynum("333444555").info()