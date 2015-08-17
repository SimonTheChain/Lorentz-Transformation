# These modules are needed to do the square root operation and to display the results with precision
from math import sqrt
from decimal import Decimal

# This sets the loop for the whole script
program = True
while program == True:


	print """
This will calculate some of the effects of Einstein's Theory of Special Relativity.
"""


# This function verifies that a number was entered
	def number_check(x):
		try:
			int(x)
		except ValueError:
			try:
				float(x)
			except ValueError:
				print "This is not a number.  Try again."
				global num_check
				num_check = False

				
# This is where the user selects the units to be used
	question1 = True
	while question1 == True:
		print """Select the unit to be used for speed:
(1) Kilometers per hour (km/h)
(2) Miles per hour (mph)
(3) Fraction of the speed of light (ex.: 0.85c)"""
		unit_velocity = raw_input("> ")

# This checks which unit was selected and sets c accordingly
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
			subquestion1 = True
			while subquestion1 == True:
				print "Expected 1, 2 or 3.  Try again? (y/n)"
				question1_answer = raw_input("> ").lower()
				if question1_answer[:1] == "y":
					print "Ok"
					subquestion1 = False
				elif question1_answer[:1] == "n":
					quit()
				else:
					print "Input unrecognized, try again."
	
	
# This is where the user inputs the value for the velocity	
	question2 = True
	while question2 == True:
		num_check_loop = True
		while num_check_loop == True:
			print "Enter your speed in %s (the speed of light in a vacuum is %s %s): " % (unit_velocity, c, unit_velocity)
			speed = raw_input("> ")
			num_check = True
			number_check(speed)
			if num_check == True:
				num_check_loop = False

# This verifies that the number entered is valid
		velocity = Decimal(speed)
		if velocity > c:
			print "You are moving faster than light! This is impossible.  Try again."
		elif velocity == c:
			print "You are travelling at exactly the speed of light, this is not allowed."
		elif velocity <= 0:
			print "You need to be in foward motion."
		else:
			question2 = False
			print "Ok"


# This is where the user inputs the value for the mass	
	weight = raw_input("Enter your mass (let's approximate to your weight, in lbs): ")

	number_check(weight)

	mass = Decimal(weight)

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

	number_check(height)

	length = Decimal(height)

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
	gamma = Decimal(1 / Decimal(sqrt(1 - ((velocity / c) ** 2))))

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

# This asks to run the script again
	print "Do you want to enter new values? (Yes/No)"
	rerun = raw_input("> ").lower()
	if rerun == "yes" or rerun == "y":
		print "Ok"
	else:
		program = False
		exit = raw_input("Thank you for using this program by Simon Lachaine.")
		exit == quit()
