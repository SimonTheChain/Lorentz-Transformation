#This module is needed to do the square root operation
import math

print "This will calculate some of the effects of Einstein's Theory of Special Relativity."

#This is where the user inputs the values
velocity = raw_input("Enter your speed in km/h: ")
weight = raw_input("Enter your mass (let's approximate to your weight, in lbs): ")
height = raw_input("Enter your height in inches: ")

#This is to convert the strings recorded above into floats
v = float(velocity)
mass = float(weight)
length = float(height)

#This is the speed of light in a vacuum in km/h
c = 1079252848800.0

#This is to calculate the Lorentz factor
gamma = 1.0 / (math.sqrt(1.0 - ((v / c) ** 2)))

#This displays the results
print """It means that:
Your mass is now %s lbs;
If you travel lying down in the direction of movement, to someone not moving your height is now %s inches;
1 year to you is %s years to someone not moving.""" % ((mass * gamma), (length / gamma), (1 * gamma))
