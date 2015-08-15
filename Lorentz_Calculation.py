print """
This will calculate some of the effects of Einstein's Theory of Special Relativity.
"""

# These modules are needed to do the square root operation and to display the results with precision
import math
import decimal

# This is the speed of light in a vacuum in km/h
c = decimal.Decimal(1079252848800)


# This is where the user inputs the value for the velocity
speed = raw_input("Enter your speed in km/h: ")

# This is to make sure a number was entered
try:
    int(speed)
except ValueError:
    try:
        float(speed)
    except ValueError:
        quit("This is not a number.")

velocity = decimal.Decimal(speed)

# This verifies that the number entered is valid
if velocity > c:
	quit("You are moving faster than light! This is impossible.")
elif velocity == c:
	quit("You are travelling at exactly the speed of light, this is not allowed.")
elif velocity <= 0:
	quit("You need to be in motion. Try again!")
else:
	print "Ok"


# This is where the user inputs the value for the mass	
weight = raw_input("Enter your mass (let's approximate to your weight, in lbs): ")

# This is to make sure a number was entered
try:
    int(weight)
except ValueError:
    try:
        float(weight)
    except ValueError:
        quit("This is not a number.")

mass = decimal.Decimal(weight)

# This verifies that the number entered is valid
if mass <= 0:
	quit("You should weigh something. Try again!")
elif mass > 500:
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
height = raw_input("Enter your height in inches: ")

# This is to make sure a number was entered
try:
    int(height)
except ValueError:
    try:
        float(height)
    except ValueError:
        quit("This is not a number.")

length = decimal.Decimal(height)

# This verifies that the number entered is valid
if length <= 0:
	quit("You should be taller than 0 inches.")
elif length > 100:
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
if (mass * gamma) == mass and (length / gamma) == length and (1 * gamma) == 1:
	quit("You're not moving fast enough to display changes.  Try again with a higher value.")
else:

# This displays the results
	print """
According to Special Relativity:
Your mass is now %s lbs;
If you travel lying down in the direction of movement, to someone not moving your height is now %s inches;
1 year to you is %s years to someone not moving.
""" % ((mass * gamma), (length / gamma), (1 * gamma))

# This is to make sure the user has time to read
exit = raw_input("Press Enter to exit program.")
exit == quit()
