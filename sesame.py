import random as rnd
from sys import argv

class Sesame(object):

	def __init__(self, height, width, percentage):
		self.height = height
		self.width = width
		self.percentage = percentage
		self.sesame_field = []
		self.flowers = ["."," "]

		self.generate()

	def generate(self):
		"""
		Generates the dot field.
		"""

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

		for i in range(self.height):
			row = []
			for j in range(self.width):
				row.append(" ")
			self.sesame_field.append(row)

		sprinkles = int(self.height * self.width * self.percentage)
		already = []

		while sprinkles > 0:
			rand_x = rnd.randrange(self.width)
			rand_y = rnd.randrange(self.height)
			if (rand_x,rand_y) in already:
				continue
			else:
				self.sesame_field[rand_y][rand_x] = "."
				sprinkles -= 1
				already.append( (rand_x,rand_y) )


	def display(self):
		vertical_bound = []
		for x in range(self.width):
			vertical_bound.append("=")
		print "="+"".join(vertical_bound)+"="
		for i in range(self.height):
			print "="+"".join(self.sesame_field[i])+"="
		print "="+"".join(vertical_bound)+"="

	def set_dimensions(self, height, width):
		self.height = height
		self.width = width
		self.generate()

	def set_percentages(self, percentage):
		self.percentage = percentage
		self.generate()

	def export(self): 
		script, filename = argv
		target = open(filename, 'w')
		target.seek(0)
		target.truncate()
		vertical_bound = []
		for x in range(self.width):
			vertical_bound.append("=")
		target.write("="+"".join(vertical_bound)+"="+"\n")
		for i in range(self.height):
			target.write("="+"".join(self.sesame_field[i])+"="+"\n")
		target.write("="+"".join(vertical_bound)+"="+"\n")
		target.close()



if __name__ == "__main__":
	sesame = Sesame(25,25,0.1)
	sesame.display()