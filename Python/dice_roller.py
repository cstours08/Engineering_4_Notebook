#Automatic Dice Roller
# Written by Corin Saint Ours

import random

x = ("roll")

while x == "roll":
	print ("your role:")
	role = random.randint(1,6)

	print (role)

	x=input("type roll to roll again and hit enter to exit:")
	print ("\n")
