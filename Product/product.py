class products(object):
	def __init__(self, price, name, weight, brand):
	 	self.price = price
	 	self.name = name
	 	self.weight = weight
	 	self.brand = brand
	 	self.status = "For sale"
	def productInfo(self):
		print "Name:", self.name
		print "Brand:", self.brand
	 	print "Cost: $", self.price
	 	print "Tax: 10%, Total:", self.price*1.1
	 	print "Weight:", self.weight, "lbs"
	 	print "Status:", self.status
	 	return self
	def sell(self):
	    self.status = "Sold"
	    return self
	def returns(self, reason, condition):
		if reason == "defective":
			self.status = "Defective"
			self.price = 0
		elif condition == "like new":
			self.status = "For Sale"
		elif condition == "used":
			self.status = "used"
			print "Discount!"
			self.price *= 0.20
		return self
bread = products(35, "Bread",2, "Finlandia").sell().returns("too big", "used").productInfo()
print "\n"
butter = products(11, "Butter", 0.5, "Organica").sell().returns("allergic", "like new").productInfo()
