PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

grade = float(raw_input("Enter the grade you got on a quiz"))
#todo fill in - and +'s
if(grade >= 90.0):
	print("You got an A")
if(grade >= 80.0 and grade < 90.0):
	print("you got a B")
if(grade >= 70.0 and grade < 80.0):
	print("you got a C")
if(grade >= 60.0 and grade < 70.0):
	print(+"you got a D")
if(grade >= 50.0 and grade < 60.0):
	print("you got an F, sorry")

