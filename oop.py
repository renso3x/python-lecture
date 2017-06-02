class Circle(object):
	pi = 3.14

	def __init__(self, rad = 1):
		self.radius = rad

	def setRadius(self, rad):
		self.radius = rad

	def area(self):
		return (self.radius**2) * Circle.pi

	def getRadius(self):
		return self.radius

	def perimeter(self):
		return (Circle.pi * 2) * self.radius

c = Circle();
c.setRadius(9)
print 'The area is ', c.area()
print 'Radius is ', c.getRadius()
print 'Perimeter is ', c.perimeter()

class Animal(object):
	def __init__(self):
		print 'Animal created'

	def whoAmI(self):
		print 'Animal'

	def eat(self):
		print 'Eating'

class Dog(Animal): #inherit from animal
	specie = 'mamal'

	def __init__(self, name, breed):
		Animal.__init__(self) #inherit from animal
		self.name = name
		self.breed = breed

	def whoAmI(self):
		print 'Dog' #inherit from animal

	def bark(self):
		return 'Roof roof!!'

	def getName(self):
		return self.name

	def myBreed(self):
		return self.breed

frank = Dog('Frank', 'Husky')
print frank.breed
print frank.eat()
print frank.whoAmI()
print frank.getName()
print frank.myBreed()
print frank.specie


#homework
class Line(object):
	def __init__(self, coord1, coord2):
		self.coord1 = coord1
		self.coord2 = coord2

	def distance(self):
		x1, y1 = self.coord1
		x2, y2 = self.coord2
		return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

	def slope(self):
		x1, y1 = self.coord1
		x2, y2 = self.coord2

		return float((y2 - y1) / (x2 - x1))


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)
print li.distance()
print li.slope()


class Cylinder(object):
	pi = 3.14

	def __init__(self, height = 1, radius = 1):
		self.height = height
		self.radius = radius

	def volume(self):
		return Cylinder.pi * (self.radius**2) * self.height

	def surface_area(self):
		return float((2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * (self.radius ** 2)))

cylinder = Cylinder(2, 3)
print cylinder.volume()
print cylinder.surface_area()
