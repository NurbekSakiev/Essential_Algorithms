from random import randint

def randomizeArray (array):
	max_i = len(array)-1
	for i in range(max_i):
		j = randint(i,max_i)
		temp = array[j]
		array[j]= array[i]
		array[i] = temp