class patients(object):
	def __init__(self, id_num, name, allergies=None):
		self.id_num = id_num
		self.name = name
		self.allergies = allergies
		self.bed = None
	def assign(self, room):
		self.bed = room 
		return self
	def display(self):
		print "ID:", self.id_num, "Name:", self.name, "Allergies:", self.allergies, "Bed number:", self.bed
		return self
Quan = patients(12, "Quan")
Craig = patients(10, "Craig", "Pine")
Dimitri = patients(9, "Dimitri")
Eric = patients(2, "Eric", "Seasonal")

class hospital(object):
	def __init__(self):
		self.patients = []
		self.beds = []
		self.hospitalname = "EverGreen"
		self.capacity = 3
		for i in range(0, self.capacity):
			self.beds.append(False)
	def admit(self, person):
		if self.capacity < 1:
			print person.name, "Sorry about that, our Hospital is full, get sick some other time"
		elif person not in self.patients:
			self.patients.append(person)
			for i in range(0, len(self.beds)):
				if self.beds[i] == False:
					person.assign(i)
					self.beds[i]= True
					break
			self.capacity -= 1
			print person.name, "You have been admitted into our Hospital" 
		else: 
			print "Hey!", person.name, " Go back to your room, stop playing games"
		return self
	def discharge(self, person):
		if person in self.patients:
			self.patients.remove(person)
			self.beds[person.bed] = False
			self.capacity += 1
			print "Bye-Bye, glad you feel beter", person.name
		else:
			print person.name, "is not currently admitted in our hospital"
		return self
	def info(self):
		print "Available rooms:", self.capacity
		return self
EverGreen = hospital()
EverGreen.admit(Quan).admit(Eric).admit(Quan).admit(Dimitri).admit(Craig).discharge(Craig).info()
Quan.display()
Craig.display()
Dimitri.display()
Eric.display()

