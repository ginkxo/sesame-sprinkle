import random as rnd
import emoji 

class Sesame(object):

	def __init__(self, height, width, percentage):
		self.height = height
		self.width = width
		self.percentage = percentage
		sesame_field = []
		flowers = ["."," "]

	def generate(self):

		if self.percentage < 0:
			self.percentage = 0
		elif self.percentage > 100:
			self.percentage = 100
		elif self.percentage > 1:
			self.percentage = self.percentage/100.0

		if self.height <= 1:
			self.height = 1

		if self.width <= 1:
			self.width = 1

		for i in range(height):
			row = []
			for j in range(width):
				row.append(" ")
			sesame_field.append(row)

		sprinkles = int(height * width * self.percentage)

		while sprinkles > 0:
			already = []
			rand_x = rnd.randrange(width)
			rand_y = rnd.randrange(height)
			if not (rand_x,rand_y) in already:
				sesame_field[rand_y][rand_x] = "."
				sprinkles =- 1
				already.append((rand_x,rand_y))

		# et cetera


	def display(self):

	def reset(self):

	def set_dimensions(self, height, width):

	def set_percentages(self, percentage):

	def export(self):
