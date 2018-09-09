#!/bin/python

def permutationCycles(permutation):

	inCycle = []
	result = 0
	
	print 'len(permutation): ', len(permutation)

	for i in range(len(permutation)):
		inCycle.append(False)
	
	print 'inCycle: ', inCycle
 
	for i in range(len(permutation)):
		print 'i: ', i
		if not inCycle[i]:
			position = i
			print 'position: ', position
			while not inCycle[position]:
				print 'inCycle[position]: ', inCycle[position]
				inCycle[position] = True
				print 'inCycle[position]: ', inCycle[position]
				print 'permutation[position]: ', permutation[position]
				position = permutation[position] - 1
				print 'position: ', position
			result += 1

	return result


permutation = [1, 3, 2, 6, 4, 5]
print permutationCycles(permutation)


print "\n----------------------\n"

permutation = [1, 2, 3]
print permutationCycles(permutation)
