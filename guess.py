#todo, change to random number
import random

answer = random.randint(0,5)

guess = int(raw_input("Enter a number, 0-5"))
if(guess > answer):
	print("Your number is too high")
elif(guess < answer):
	print("Your number is too low")
elif(guess == answer):
	print("Good job! you got my numnber!")

answer = random.randint(0,5)

guess = int(raw_input("Enter a number again, 0-5"))
if(guess > answer):
	print("Your number is too high")
elif(guess < answer):
	print("Your number is too low")
elif(guess == answer):
	print("yes, you guessed my number")

