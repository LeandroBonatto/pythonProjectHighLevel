# define radius value
import math

radius = 10

# radius = input('Please enter a radius: '))
# radius = float(input('Please enter a radius: '))
# radius = int(input('Please enter a radius: '))

# radius = eval(input('Please enter a radius: '))

radius, diameter = eval(input('Please enter a radius and diameter: '))

# calculate area of the circle
area = radius * radius * 3.14
area = radius * radius * math.pi

# printing the area
print('The area of the circle with radius', radius, 'is', area)
# print('The area of the circle is' + str(area)) - +  concatenation

