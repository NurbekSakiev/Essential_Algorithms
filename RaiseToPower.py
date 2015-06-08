def RaiseToPower(A,P):
	n = 1
	result = 1
	while (P >=1):
		if (P % 2 == 1):
			result = result * A
		P = P/2
		A = A*A
	return result

print RaiseToPower(7,10040)



