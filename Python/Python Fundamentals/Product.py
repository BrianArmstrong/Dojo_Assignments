class Product(object):
	def __init__(self, price, item_name, weight, brand, status="for sale"):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = status
		# print self
	def display_all(self):
		print self
		return self
	def __repr__(self):
		return "Price: ${}, Item name: {}, Weight: {}, Brand: {}, Status: {}".format(self.price, self.item_name, self.weight, self.brand, self.status)
	def sold(self):
		self.status = "Sold"
		print self
		return self
	def tax(self):
		self.price += self.price * .10
		print self
		return self
	def returns(self, condition):
		self.condition = condition
		if self.condition == "defective":
			self.price = 0
			self.status = "defective"
			# return self
		elif self.condition == "in box":
			self.status = "like new"
			# return self
		elif self.condition == "opened":
			self.status = "used"
			self.price = (self.price *.80)
		return self




if __name__ == "__main__":
	Motor_oil = Product(price = 25, item_name = "Motor Oil", weight = "1 quart", brand = "Penzoil")
	# print Motor_oil
	
print Motor_oil.returns("opened")