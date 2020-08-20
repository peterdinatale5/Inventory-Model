#tic tac toe
import random

notguessed = True
attempt = 0
number = random.choice(['1','2','3'])
apple = list("a")
word = "apple"

class Fruit:
	def __init__(self, Type, price, stock):
		self.Type = Type
		self.price = price
		self.stock = stock
		self.fruits = []

	def get_stock(self):
		return self.stock

	def get_price(self):
		return self.price

	def add_fruit(self, fruit):
		self.fruit = fruit
		if len(self.fruit) < self.max_students:
			self.students.append(student)
			return True
		return False

#class Bills:
apple = Fruit("fruit", "five dollars", 5)
pear = Fruit("fruit", "seven dollars", 2)

def attempt_count():
	if attempt < 3:
		notguessed = True
	else:
		notguessed = False
		print("game over")

def choose_fruit():
	prompt1 = input("pick an item (a) apple (b) pear (c) carrot:  ").lower()
	if prompt1 == "apple":
		print("hi")
		print(apple.get_stock())
	if prompt1 == "pear":
		print("pear stock")
		print(pear.get_stock())
		for x in range(0, 10, 1):
			print(x)

while notguessed and attempt < 3:
	response = input("enter passcode for store: ")
	if response == number:
		print("yay")
		print("welcome to the fruit shop")
		notguessed = False
	elif response != number:
		print("no")
		attempt += 1
		attempt_count()

choose_fruit()



