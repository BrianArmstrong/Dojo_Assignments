class Car(object):
	def __init__(self, price, speed, fuel, mileage, tax=.12):
		if price >= 10000:
			tax = .15
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = tax
		# print self
	def display_all(self):
		print self
		return self
	def __repr__(self):
		return "Price: ${}, Speed: {}mph, Fuel: {}, Mileage: {}mpg, Tax: {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

if __name__ == "__main__":
	Satan = Car(price = 666, speed = 66.6, fuel = "Full", mileage = 66.6)
	Angel = Car(price = 777, speed = 77.7, fuel = "Empty", mileage = 7.77)
	Brian = Car(price = 26000, speed = 140, fuel = "Full", mileage = 90)
	Toro = Car(price = 600, speed = 40, fuel = "Almost Full", mileage = 50)
	Rabbit = Car(price = 50000, speed = 100, fuel = "Almost Empty", mileage = 90)
	Rocket = Car(price = 100000, speed = 640, fuel = 500, mileage = 2)


Satan