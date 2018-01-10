#Assignment: Animal
class Animal(object):
	def __init__(self, name, health=100):
		self.name = name
		self.health = health
	def displayHealth(self):
		print self
		return self
	def walk(self, walks):
		self.health -= (1 * walks)
		return self
	def run(self, runs):
		self.health -= (5 * runs)
		return self
	def __repr__(self):
		return "Health: {}, Name: {}".format(self.health, self.name)




class Dog(Animal):
	def dogHealth(self):
		self.health = 150
		return self
	def petting(self, pettings):
		self.health += (5 * pettings)
		return self


class Dragon(Animal):
	def dragonHealth(self):
		self.health = 170
		return self
	def fly(self, flights):
		self.health -= (10 * flights)

# Animal("dog", 100).walk(3).run(3).displayHealth()
d = Dog("Poodle").dogHealth().walk(3).run(2).petting(3)
print d

g = Dragon()












