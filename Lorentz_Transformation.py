# These modules are needed to do the square root operation
# and to display the results with precision
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

# This function asks a question and verifies the input
def question_loop(question_number, weight_or_height, text, \
mass_or_length, text_zero, value_high, text_high):	
	question_number = True
	while question_number == True:
		weight_or_height = 0
		number_check_loop(weight_or_height, text)
		weight_or_height = z
		mass_or_length = Decimal(weight_or_height)
		if mass_or_length <= 0:
			print text_zero
		elif mass_or_length > value_high:
			answer1 = raw_input(text_high).lower()
			if answer1[:1] == "y":
				question_number = False
				print "Ok\n"
			elif answer1[:1] == "n":
				print "Try again then.\n"
			else:
				print "Unrecognized input.  Try again.\n"
		else:
			question_number = False
			global zz
			zz = mass_or_length
			print "Ok\n"
			
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
		number_check_loop(speed, "\nEnter your speed in %s (the speed of light in a vacuum is %s %s)\n> " \
		% (unit_velocity, c, unit_velocity))
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
	question3, weight, mass = 0, 0, 0
	question_loop(question3, weight, "Enter your mass (let's approximate to your weight, in lbs):\n> ", \
	mass, "You should weigh something. Try again.\n", 500, "Are you sure you weigh that much? (y/n)\n> ")
	mass = zz

	
# This is where the user inputs the value for the length
	question4, height, length = 0, 0, 0
	question_loop(question4, height, "Enter your height in inches:\n> ", length, \
	"You should be taller than 0 inches.  Try again.\n", 100, "Are you sure you are that tall? (y/n)\n>")
	length = zz

	
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
