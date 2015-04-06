# Essential Algorithms
# Calculating Greatest Common Divisor
# author: Nurbek Sakiev

def GCD(a,b):
	if (b == 0):
		return a
	while b!=0:
		rem = a%b
		a = b
		b = rem
	return a


