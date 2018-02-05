class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def bikeInfo(self):
		print "Cost: $", self.price
		print "Max-Speed:", self.max_speed, "MPH"
		print "Miles:", self.miles
	def ride(self):
	  print "Riding..."
	  self.miles += 10
	def reverse(self):
	  print "Reversing..."
	  if self.miles >= 5:
	    self.miles -= 5
motodyne = Bike("2000", "60")
motodyne.ride()
motodyne.ride()
motodyne.ride()
motodyne.reverse()
motodyne.bikeInfo()
rocketbunny = Bike("2500", "70")
rocketbunny.ride()
rocketbunny.ride()
rocketbunny.reverse()
rocketbunny.reverse()
rocketbunny.bikeInfo()
chevy = Bike("1000", "25")
chevy.reverse()
chevy.reverse()
chevy.reverse()
chevy.bikeInfo()