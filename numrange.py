number = int(raw_input("enter a number, 1-1000"))
lowerbound = 40
upperbound = 60

if(number >= 40 and number <= 60):
	print("you found the number")

elif(number < 40 or number > 60):
	print("you did not find the number, nice try tho")
else:
	print("what was that?")

