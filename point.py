import math

class Point:

	def __init__(self, param_x=0.0, param_y=0.0):

		self.x = param_x
		self.y = param_y

	def __str__(self):

		return str(self.x) + ", " + str(self.y)

	def distance_from_origin(self):

		return math.sqrt(x*x + y*y)

	def distance_from_point(self, other):

		diff_x = self.x - other.x
		diff_y = self.y - other.y

		return math.sqrt(diff_x*diff_x + diff_y*diff_y)
