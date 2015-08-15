print """
This will calculate some of the effects of Einstein's Theory of Special Relativity.
"""

# These modules are needed to do the square root operation and to display the results with precision
import math
import decimal


# This is where the user selects the units to be used
unit_velocity = raw_input("""Select the unit to be used for speed:
(1) Kilometers per hour (km/h)
(2) Miles per hour (mph)
(3) Fraction of the speed of light (ex.: 0.85c)
> """)

# This checks which unit was selected and sets c accordingly
if str(unit_velocity) == "1":
	unit_velocity = "km/h"
	c = decimal.Decimal(1079252848800)
elif str(unit_velocity) == "2":
	unit_velocity = "mph"
	c = decimal.Decimal(670616629)
elif str(unit_velocity) == "3":
	unit_velocity = "c"
	c = decimal.Decimal(1)
else:
	exit = raw_input("Expected 1, 2 or 3.  Press Enter.")
	exit == quit()

	
# This is where the user inputs the value for the velocity
print "Enter your speed in %s (the speed of light in a vacuum is %s %s): " % (unit_velocity, c, unit_velocity)
speed = decimal.Decimal(raw_input())

# This is to make sure a number was entered
try:
    int(speed)
except ValueError:
    try:
        float(speed)
    except ValueError:
        exit = raw_input("This is not a number.  Press Enter.")
	exit == quit()
		
velocity = decimal.Decimal(speed)

# This verifies that the number entered is valid
if velocity > c:
	exit = raw_input("You are moving faster than light! This is impossible.  Press Enter.")
	exit == quit()
elif velocity == c:
	exit = raw_input("You are travelling at exactly the speed of light, this is not allowed.  Press Enter.")
	exit == quit()
elif velocity <= 0:
	exit = raw_input("You need to be in foward motion. Press Enter.")
	exit == quit()
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
        exit = raw_input("This is not a number.  Press Enter.")
	exit == quit()

mass = decimal.Decimal(weight)

# This verifies that the number entered is valid
if mass <= 0:
	exit = raw_input("You should weigh something. Press Enter.")
	exit == quit()
elif mass > 500:
	answer1 = raw_input("Are you sure you weigh that much? ").lower()
	if answer1 == "yes" or answer1 == "y":
		print "Ok"
	elif answer1 == "no" or answer1 == "n":
		exit = raw_input("I thought so.  Press Enter.")
		exit == quit()
	else:
		exit = raw_input("Unrecognized input.  Press Enter.")
		exit == quit()
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
        exit = raw_input("This is not a number.  Press Enter.")
	exit == quit()

length = decimal.Decimal(height)

# This verifies that the number entered is valid
if length <= 0:
	exit = raw_input("You should be taller than 0 inches.  Press Enter.")
	exit == quit()
elif length > 100:
	answer2 = raw_input("Are you sure you are that tall? ").lower()
	if answer2 == "yes" or answer2 == "y":
		print "Ok"
	elif answer2 == "no" or answer2 == "n":
		exit = raw_input("Try again then.  Press Enter.")
		exit == quit()
	else:
		exit = raw_input("Unrecognized input.  Press Enter.")
		exit == quit()
else:
	print "Ok"

# This is to calculate the Lorentz factor
gamma = decimal.Decimal(1 / (math.sqrt(1 - ((velocity / c) ** 2))))

# This verifies that there are changes to report
if (mass * gamma) == mass and (length / gamma) == length and (1 * gamma) == 1:
	exit = raw_input("You're not moving fast enough to display changes.  Try again with a higher value.  Press Enter.")
	exit == quit()
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
