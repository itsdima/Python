class car(object):
	def __init__(self, price, max_speed, fuel, mileage):
		self.price = price
		self.max_speed = max_speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = 0
	def carInfo(self):
		print "Cost: $", self.price
		print "Speed:", self.max_speed, "MPH"
		print "Fuel:", self.fuel 
		print "Mileage:", self.mileage, "MPG"
		if self.price > 10000:
			print "Tax: 15%"
		else: 
			print "Tax: 12%"
Infiniti = car(15000, 160, "full", 20)
BMW = car(25000, 180, "empty", 25)
AMG = car(30000, 200, "half", 15)
Lexus = car(40000, 175, "full", 28)
Lada = car(500, 40, "empty", 30)
BRZ = car(20000, 120, "full", 30)
BMW.carInfo()
Infiniti.carInfo()
AMG.carInfo()
Lexus.carInfo()
Lada.carInfo()
BRZ.carInfo()