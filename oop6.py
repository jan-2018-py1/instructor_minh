myList = [1,2,3,4,5]

myList.append(6)
myList.pop()

minh = {
	"name":"minh",
	"location":"Seattle, WA",
	"gender":"Male"
}

# myDictionary.keys().  

# print minh["name"]

jeff = {
	"name":"jeff",
	"location":"Seattle, WA",
	"gender":"Male"
}
#Class
#Instance - Creation(copy) of a class
#Method - function of a class 
#Inheritance
# Make (Toyota) -> Model (Corolla) -> Year (2017)
# Object -> Mammal -> Human 

#Chaining

class Mammal(object):
	def __init__(self, live_born, four_limbed=True, hairy=True):
		self.live_born = live_born
		self.four_limbed = four_limbed
		self.hairy = hairy
	def printData(self):
		print "live:",self.live_born
		print "fourlimbed:",self.four_limbed
		print "hairy:",self.hairy

class Human(Mammal):
	def __init__(self, name, location, gender):
		super(Human, self).__init__(True)
		self.name = name
		self.location = location
		self.gender = gender
		self.favorite_food = ["wings", "pizza", "tacos", "oreos"]
	def greet(self):
		print "Hello, my name is {}".format(self.name)
	def printData(self):
		print "name:" + self.name
		print "location:" + self.location
		print "gender:" + self.gender
		print self
		return self
	def removeFavorite(self, favorite):
		for i in range(0, len(self.favorite_food)):
			if self.favorite_food[i] == favorite:
				self.favorite_food.pop(i)
				break
		print self.favorite_food
		return self
	def addFavorite(self, favorite):
		self.favorite_food.append(favorite)
		print self.favorite_food
		return self

# minh = Human(True)
# print minh.hairy
minh = Human("minh", "Seattle, WA", "Male")
minh.removeFavorite("wings").removeFavorite("tacos").addFavorite("clam chowder")
# $("#myH1").click(function(){

# })
# print dir(minh)
# # print minh
# # print minh.name
# # print minh.location
# # jeff = Human("jeff", "Seattle, WA", "Male")
# # print jeff
# jeff.greet()
# minh.greet()




