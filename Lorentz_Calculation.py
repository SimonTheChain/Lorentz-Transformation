print """
This will calculate some of the effects of Einstein's Theory of Special Relativity.
"""

# These modules are needed to do the square root operation and to display the results with precision
import math
import decimal

# This is the speed of light in a vacuum in km/h
c = decimal.Decimal(1079252848800)

# This is where the user inputs the value for the velocity
velocity = decimal.Decimal(raw_input("Enter your speed in km/h: "))
if velocity > c:
	quit("You are moving faster than light! This is impossible.")
elif velocity == c:
	quit("You are travelling at exactly the speed of light, this is not allowed.")
elif velocity <= 0:
	quit("You need to be in motion. Try again!")
else:
	print "Ok"

# This is where the user inputs the value for the mass	
weight = decimal.Decimal(raw_input("Enter your mass (let's approximate to your weight, in lbs): "))
if weight <= 0:
	quit("You should weigh something. Try again!")
elif weight > 500:
	answer1 = raw_input("Are you sure you weigh that much? ").lower()
	if answer1 == "yes" or answer1 == "y":
		print "Ok"
	elif answer1 == "no" or answer1 == "n":
		quit("I thought so.")
	else:
		quit("Unrecognized input.")
else:
	print "Ok"

# This is where the user inputs the value for the length
height = decimal.Decimal(raw_input("Enter your height in inches: "))
if height <= 0:
	quit("You should be taller than 0 inches.")
elif height > 100:
	answer2 = raw_input("Are you sure you are that tall? ").lower()
	if answer2 == "yes" or answer2 == "y":
		print "Ok"
	elif answer2 == "no" or answer2 == "n":
		quit("Try again then.")
	else:
		quit("Unrecognized input.")
else:
	print "Ok"

# This is to calculate the Lorentz factor
gamma = decimal.Decimal(1 / (math.sqrt(1 - ((velocity / c) ** 2))))

# This verifies that there are changes to report
if (weight * gamma) == weight and (height / gamma) == height and (1 * gamma) == 1:
	quit("You're not moving fast enough to display changes.  Try again with a higher value.")
else:

# This displays the results
	print """
According to Special Relativity:
Your mass is now %s lbs;
If you travel lying down in the direction of movement, to someone not moving your height is now %s inches;
1 year to you is %s years to someone not moving.
""" % ((weight * gamma), (height / gamma), (1 * gamma))
