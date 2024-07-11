#Write a script in Python that accepts radius of a circle and prints its area & perimeter.
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
print ("The perimeter of the circle with radius " + str(r) + " is " + str(2*pi*r))