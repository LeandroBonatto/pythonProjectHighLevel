# define radius value
import math

radius = 10

radius, diameter = eval(input('Please enter a radius and diameter: '))

# calculate area
area = radius * radius * math.pi

# print area
print('The area of the circle with radius', radius, 'is', area)
print('The area of the circle with radius', str(radius) + ' is ' + str(area))