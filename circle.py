from point import Point
import math

class Circle:

	def __init__(self, center_x=0.0, center_y=0.0, radius=0.0):

		self.center = Point(center_x, center_y)

		if radius == 0:

			raise ValueError("Radius can not be zero.")

		self.radius = radius

	def __str__(self):

		return "Circle with center at " + str(self.center.x) + ", " +\
		str(self.center.y) + " and radius " + str(self.radius)

	def find_intersection(self, other):

		# Find the intersection of self and other

		r1 = self.radius 
		r2 = other.radius

		print self
		print other

		# 2 must be the circle on the right

		if self.center.x <= other.center.x:

			x1 = self.center.x
			y1 = self.center.y
			x2 = other.center.x
			y2 = other.center.y

		else:

			x2 = self.center.x
			y2 = self.center.y
			x1 = other.center.x
			y1 = other.center.y
		
		print x1, y1, x2, y2

		distance_bet_centers = self.center.distance_from_point(other.center)

		sum_radii = r1 + r2

		separate = distance_bet_centers > sum_radii
		contained = distance_bet_centers < abs(r1 - r2)
		tangential = distance_bet_centers == sum_radii
		two_intersection_points = distance_bet_centers < sum_radii

		if separate or contained:

			return None

		elif tangential:

			# Tangential case
			# One Point to be returned

			return None

		elif two_intersection_points:

			# Two points in this case
			# A list of two points to be returned

			diff_distance = (r1*r1 - r2*r2)/ distance_bet_centers
			d1 = (diff_distance + distance_bet_centers) / 2
			d2 = (distance_bet_centers - diff_distance) / 2
			h = math.sqrt(r1*r1 - d1*d1)

			# x_c_1, y_c_1 is the point inside the common area

			d = distance_bet_centers

			x_c = x1 + d1 / d * (x2 - x1)
			y_c = y1 + d1 / d * (y2 - y1)

			m = (y2 - y1) / (x2 - x1)
			k1 = m * y_c + x_c

			# Quadratic to find the value of the intersection points

			a = 1 + m*m

			b = -2*y_c - 2*m*k1 + 2*m*x_c

			c = y_c*y_c + k1*k1 + x_c*x_c - 2*k1*x_c - h*h

			D = b*b - 4*a*c

			if D < 0:

				raise ValueError("Discriminant can't be negative.")

			y_i_1 = (-b + math.sqrt(D))/(2*a)
			y_i_2 = (-b - math.sqrt(D))/(2*a)

			x_i_1 = k1 - m * y_i_1
			x_i_2 = k1 - m * y_i_2

			g = Point(x_i_1, y_i_1)
			h = Point(x_i_2, y_i_2)

			print d, m
			return [g, h]

c1 = Circle(0, 0, 4)
c2 = Circle(2, 3, 5)

intersection = c1.find_intersection(c2)

print intersection[0]
print intersection[1]