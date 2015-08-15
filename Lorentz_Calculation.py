print """
This will calculate some of the effects of Einstein's Theory of Special Relativity.
"""

#This module is needed to do the square root operation
import math

#This is the speed of light in a vacuum in km/h
c = 1079252848800.0

#This is where the user inputs the value for the velocity
velocity = raw_input("Enter your speed in km/h: ")
if float(velocity) > c:
	quit("You are moving faster than light! This is impossible.")
elif float(velocity) == c:
	quit("You are travelling at exactly the speed of light, this is not allowed.")
elif float(velocity) <= 0:
	quit("You need to be in motion. Try again!")
else:
	print "Ok"

#This is where the user inputs the value for the mass	
weight = raw_input("Enter your mass (let's approximate to your weight, in lbs): ")
if int(weight) <= 0:
	quit("You should weigh something. Try again!")
elif int(weight) > 500:
	answer1 = raw_input("Are you sure you weigh that much? ").lower()
	if answer1 == "yes" or answer1 == "y":
		print "Ok"
	elif answer1 == "no" or answer1 == "n":
		quit("I thought so.")
	else:
		quit("Unrecognized input.")
else:
	print "Ok"

#This is where the user inputs the value for the length
height = raw_input("Enter your height in inches: ")
if int(height) <= 0:
	print "You should be taller than 0 inches."
	quit()
elif int(height) > 100:
	answer2 = raw_input("Are you sure you are that tall? ").lower()
	if answer2 == "yes" or answer2 =="y":
		print "Ok"
	elif answer2 == "no" or answer2 == "n":
		quit("Try again then.")
	else:
		quit("Unrecognized input.")
else:
	print "Ok"

#This is to convert the strings recorded above into floats
v = float(velocity)
mass = float(weight)
length = float(height)

#This is to calculate the Lorentz factor
gamma = 1.0 / (math.sqrt(1.0 - ((v / c) ** 2)))

#This displays the results
print """
According to Special Relativity:
Your mass is now %s lbs;
If you travel lying down in the direction of movement, to someone not moving your height is now %s inches;
1 year to you is %s years to someone not moving.
""" % ((mass * gamma), (length / gamma), (1 * gamma))
