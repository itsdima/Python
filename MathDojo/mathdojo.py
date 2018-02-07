class MathDojo(object):
	def __init__(self):
		self.sum = 0
	def add(self, *args):
		for i in range(0, len(args)):
			if isinstance(args[i], int):
				self.sum += args[i]
			elif isinstance(args[i], list or tuple): 
				for x in range(0, len(args[i])):
					self.sum+= args[i][x]
			elif isinstance(args[i], tuple):
				for y in range(0, len(args[i])):
					self.sum += args[i][y]
		return self
	def subtract(self, *args):
		for i in range(0, len(args)):
			if isinstance(args[i], int):
				self.sum -= args[i]
			elif isinstance(args[i], list): 
				for x in range(0, len(args[i])):
					self.sum -= args[i][x]
			elif isinstance(args[i], tuple):
				for y in range(0, len(args[i])):
					self.sum -= args[i][y]
		return self
	def result(self):
		print self.sum 
		return self
md = MathDojo().add([1],3,4).add([3,5,7,8],(2, 2),[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result()