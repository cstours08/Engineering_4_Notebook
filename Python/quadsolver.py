# Quadratic Solver, "Solves your quads no probs"
# Written by Corin Saint Ours

import cmath

print("This is the Quadratic Solver")
print("Enter the coefficients for standard form")
print("Ax^2 + Bx + C")
print("\n")

def doMath(a,b,c):
	d=(b**2)-(4*a*c)
	sol1 = (-b-cmath.sqrt(d))/(2*a)
	sol2 = (-b+cmath.sqrt(d))/(2*a)
	print("The Answers are:")
	print(sol1)
	print(sol2)

coe_a = int(input("Coefficient A = "))
coe_b = int(input("Coefficient B = "))
coe_c = int(input("Coefficient C = "))

doMath(coe_a,coe_b,coe_c)
