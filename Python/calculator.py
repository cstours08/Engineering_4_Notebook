#Calculator program
# Written by Corin Saint Ours

def doMath(a,b): #this creates the function that I call upon later in the code
	print("Sum:", a + b)
	print("Difference:", a - b)
	print("Product:", a * b)
	print("Quotient:", round(a/b, 2))
	print("Modulo:", a % b) # All of this is what happens when I call upon
				# the doMath function

number_1 = float(input("First Number:")) #these two lines simply ask for inputs
number_2 = float(input("Second Number:")) #the float function allows decimals
					# to work as well

doMath(number_1,number_2)
# This line takes the 2 inputs and calls upon the doMath function while 
#while also fromatting the 2 inputs in a way that the doMath function can use.

