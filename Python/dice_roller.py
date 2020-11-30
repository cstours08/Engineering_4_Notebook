
#Automatic Dice Roller
# Written by Corin Saint Ours

import random

x = ("roll") #this gives x a specific input to look for

while x == "roll": #this is what occurs when the correct input is found
	print ("your role:")
	role = random.randint(1,6) #this selects a random number

	print (role)

	x=input("type roll to roll again and hit enter to exit:") 
	#this looks for the next input and gives instructions
	print ("\n")
