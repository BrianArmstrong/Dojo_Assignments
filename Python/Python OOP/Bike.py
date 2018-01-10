# Assignment: Bike

class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def display_info(self):
		print self
		return self
	def __repr__(self):
		return "Price: {}, Max_speed: {}, Miles: {},".format(self.price, self.max_speed, self.miles)
	# def displayInfo(self):
	# 	print "Price: {}, Max_speed: {}, Miles: {},".format(self.price, self.max_speed, self.miles)
	# 	return self
		#.format puts a variabe into an object to be printed as a whole string
	def ride(self,times=1):
		self.miles += (10* times)
		print "Riding! Total miles ridden: {}".format(self.miles)
		return self
		# 	print "Riding! Total miles ridden: {}".format(ride)
		# return ride
	def reverse(self,times=1):
		self.miles -= (5 * times)
		if self.miles < 0:
			self.miles = 0
		print "Reversing! Total miles: {}".format(self.miles)
		return self

if __name__ == "__main__":
	brian = Bike(price = 420, max_speed = 666)
	bob = Bike(price = 321, max_speed = 444)
	bruce = Bike(price = 276, max_speed = 222)


bob.ride(3).reverse(10).display_info()
