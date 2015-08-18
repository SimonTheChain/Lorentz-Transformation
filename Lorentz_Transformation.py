# These modules are needed to do the square root operation and to display the results with precision
from math import sqrt
from decimal import Decimal

# This function verifies that a number was entered
def number_check_loop(x, y):
	num_check_loop = True
	while num_check_loop == True:				
		x = raw_input(y)	
		num_check = True
		try:
			int(x)
		except ValueError:
			try:
				float(x)
			except ValueError:
				print "This is not a number.  Try again.\n"
				num_check = False
		global z
		z = x
		if num_check == True:
			num_check_loop = False
			
# This sets the loop for the whole script
program = True
while program == True:

				

	print """
This will calculate some of the effects of Einstein's Theory of Special Relativity.
"""



# This is where the user selects the units to be used
	question1 = True
	while question1 == True:
		unit_velocity = raw_input("""Select the unit to be used for speed:
(1) Kilometers per hour (km/h)
(2) Miles per hour (mph)
(3) Fraction of the speed of light (ex.: 0.85c)\n> """)
		if str(unit_velocity) == "1":
			unit_velocity = "km/h"
			c = Decimal(1079252848800)
			question1 = False
		elif str(unit_velocity) == "2":
			unit_velocity = "mph"
			c = Decimal(670616629)
			question1 = False
		elif str(unit_velocity) == "3":
			unit_velocity = "c"
			c = Decimal(1)
			question1 = False
		else:
			print "Expected 1, 2 or 3.  Try again.\n"
	
	
# This is where the user inputs the value for the velocity	
	question2 = True
	while question2 == True:
		speed = 0
		number_check_loop(speed, "\nEnter your speed in %s (the speed of light in a vacuum is %s %s)\n> " % (unit_velocity, c, unit_velocity))
		speed = z

# This verifies that the number entered is valid
		velocity = Decimal(speed)
		if velocity > c:
			print "\nYou are moving faster than light! This is impossible.  Try again."
		elif velocity == c:
			print "\nYou are travelling at exactly the speed of light, this is not allowed."
		elif velocity <= 0:
			print "\nYou need to be in foward motion."
		else:
			question2 = False
			print "Ok\n"


# This is where the user inputs the value for the mass	
	question3 = True
	while question3 == True:
		weight = 0
		number_check_loop(weight, "Enter your mass (let's approximate to your weight, in lbs):\n> ")
		weight = z

# This verifies that the number entered is valid
		mass = Decimal(weight)
		if mass <= 0:
			print "You should weigh something. Try again.\n"
		elif mass > 500:
			answer1 = raw_input("Are you sure you weigh that much? (y/n)\n> ").lower()
			if answer1[:1] == "y":
				question3 = False
				print "Ok\n"
			elif answer1[:1] == "n":
				print "I thought so.  Try again.\n"
			else:
				print "Unrecognized input.  Try again.\n"
		else:
			question3 = False
			print "Ok\n"

	
# This is where the user inputs the value for the length
	question4 = True
	while question4 == True:
		height = 0
		number_check_loop(height, "Enter your height in inches:\n> ")
		height = z

# This verifies that the number entered is valid
		length = Decimal(height)
		if length <= 0:
			print "You should be taller than 0 inches.  Try again.\n"
		elif length > 100:
			answer2 = raw_input("Are you sure you are that tall? (y/n)\n>").lower()
			if answer2[:1] == "y":
				question4 = False
				print "Ok\n"
			elif answer2[:1] == "n":
				print "Try again then.\n"
			else:
				print "Unrecognized input."
		else:
			question4 = False
			print "Ok\n"

	
# This is to calculate the Lorentz factor
	gamma = Decimal(1 / Decimal(sqrt(1 - ((velocity / c) ** 2))))

# This verifies that there are changes to report
	if (mass * gamma) == mass and (length / gamma) == length and (1 * gamma) == 1:
		print "\nYou're not moving fast enough to display changes.\n"
	else:

# This displays the results
		print """
According to Special Relativity:
Your mass is now %s lbs;
If you travel lying down in the direction of movement, to someone not moving your height is now %s inches;
1 year to you is %s years to someone not moving.
""" % ((mass * gamma), (length / gamma), (1 * gamma))

# This asks to run the script again
	exit_question = True
	while exit_question == True:
		rerun = raw_input("Do you want to enter new values? (y/n)\n> ").lower()
		if rerun[:1] == "y":
			exit_question = False
			print "Ok"
		elif rerun[:1] != "y" and rerun[:1] != "n":
			print "Unrecognized input, please try again.\n"
		else:
			exit_question = False
			program = False
			raw_input("\nThank you for using this program by Simon Lachaine.\n")
			quit()
