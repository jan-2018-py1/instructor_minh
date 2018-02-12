
# myList = [1,2,3,4,5]<--- a set of data
# for i in myList:
# 	print myList[i]

# sum(myList)

greg = {
	"name":"Greg Weber",
	"gender":"Male",
	"location":"Portland, OR"
}

# print greg["name"]
# print greg["gender"]
# print greg["location"]

joseph = {
	"name":"Joseph Mumford",
	"gender":"Male",
	"location":"Tulsa, OK"
}

minh = {
	"name":"Minh Nguyen",
	"gender":"Male",
	"location":"Seattle, WA"
}

# print dir(minh)

minh["name"]
# Class
# Instances
# Methods
# Inheritance #what do i get from my parent class
# Chaining Methods
# self is referring to the instance you are creating
class Primate(object):
	def __init__(self, four_limbed=True):
		self.four_limbed = four_limbed
		self.hair = True

	def printSelf(self):
		print "I am a {}".format(type(self))
		print self
		return self

def createHuman(name, gender, location):
	return Human(name, gender, location)
class Human(Primate): #
	def __init__(self, name, gender, location, four_limbed=True):
		super(Human, self).__init__(four_limbed)
		self.name = name
		self.gender = gender
		self.location = location
		self.favorite_food = ["pizzaa", "sushi", "apples", "cheeseburger", "salads", "chocolate", "wings"]
	def greet(self):
		print "Hello, my name is {}".format(self.name)
	def removeFavoriteFood(self, food_item):
		for i in range(len(self.favorite_food)):
			if self.favorite_food[i] == food_item:
				self.favorite_food.pop(i)
				break
		print self.favorite_food
		print self

greg = Human("Greg Weber", "Male", "Portland, OR")
print greg
greg.removeFavoriteFood("wings").removeFavoriteFood("apples")
# print greg.four_limbed
# print greg.name
# print greg.gender
# print greg.location
# greg.printSelf()


