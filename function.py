PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREY = '\033[90m'
RESET = '\033[0m'

def printred(message):
	print(RED + message + RESET)
def printred(message):
	print(GREEN + message + RESET)
def printyellow(message):
	print(YELLOW + message + RESET)
def printgreen(message):
	print()
	print(GREEN + message + RESET)
	print()
def printrgy(message):
	LetterIndex = 0
	newmessage = ""
	while(LetterIndex < len(message)):
		if(LetterIndex % 3 == 0):
			newmessage += RED
		elif(LetterIndex % 3 == 1):
			newmessage += GREEN
		elif(LetterIndex % 3 == 2):
			newmessage += YELLOW
		newmessage = newmessage + message[LetterIndex]
		LetterIndex +=1
	print(newmessage + RESET)
printrgy("Jack was able to go to school not being late to work")
for x in range(10):
	printyellow("hello")
	printyellow("goodbye")


#printred("Hello")
#printgreen("Merry")
#printred("Christmas!!!")
#printred("wait, how does this work?")
