class animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def status(self):
		print self.name, self.health
		return self 
class Dog(animal):
	def __init__(self, name):
		super(Dog, self).__init__(name, 150)
	def pet(self):
		self.health += 5
		return self
class Dragon(animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name, 170)
	def fly(self):
		self.health -= 10
		return self
	def status(self):
		super(Dragon, self).status()
		print "I am a Dragon"


cat = animal("Berta", 100).walk().walk().walk().run().run().status()
print ""
pup = Dog("Dude").walk().walk().walk().run().run().pet().status()
print ""
drg = Dragon("Skiye").fly().fly().fly().status()
print ""
