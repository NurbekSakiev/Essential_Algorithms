// Algorithms
// Merge Sort
// author: Nurbek Sakiev

def mergeSort(list_):
	if (len(list_) <= 1):
		return list_
	mid = len(list_)//2
	first = mergeSort(list_[:mid])
	second = mergeSort(list_[mid:])
	return list(merge(first,second))

def merge(list1, list2):
	i=j=0
	last = []

	while (i <len(list1) and j<len(list2)):
		if(list1[i] < list2[j]):
			last.append(list1[i])
			i=i+1
		else:
			last.append(list2[j])
			j = j+1
	if list1:
		last.extend(list1[i:])
	if list2:
		last.extend(list2[j:])
	return last

test = [5,3,2,6,7,8,1,9]
print mergeSort(test)