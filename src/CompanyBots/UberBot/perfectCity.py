import math




def perfectCity(departure, destination):

	distance = getBestDistance(0.0, departure, destination)

	return distance




def getBestDistance(distance=0, departure=[], destination=[]):

	if departure == destination:
		return distance


	if departure[0] == destination[0]:
		return abs(departure[1] - destination[1])

	elif departure[1] == destination[1]:
		return abs(departure[0] - destination[0])


	for n in range(len(departure)):

		if int(departure[n]) == int(destination[n]):
			upgradePoint = 0

			fracDeparture, wholeDeparture = math.modf(departure[n])
			fracDestination, wholeDestination = math.modf(destination[n])

			if (fracDeparture + fracDestination) > 1.0:
				upgradePoint = 1
				distance += 2 - (fracDeparture + fracDestination)
			else:
				distance += fracDeparture + fracDestination


			departure[n] = wholeDeparture + upgradePoint
			destination[n] = wholeDestination + upgradePoint

		distance += abs(departure[n] - destination[n])

	return distance








#~ # TEST: Originals test cases

#~ departure = [0.4, 1]
#~ destination = [0.9, 3]
#~ print perfectCity(departure, destination)
#~ print '2.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [2.4, 1]
#~ destination = [5, 7.3]
#~ print perfectCity(departure, destination)
#~ print '8.9'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [0, 0.2]
#~ destination = [7, 0.5]
#~ print perfectCity(departure, destination)
#~ print '7.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [0.9, 6]
#~ destination = [1.1, 5]
#~ print perfectCity(departure, destination)
#~ print '1.2'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [0, 0.4]
#~ destination = [1, 0.6]
#~ print perfectCity(departure, destination)
#~ print '2.0'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'






#~ # TEST: Same to the test case #1. Check all possible directions in the same case. Update the decimal point to 1

#~ # When both X's are decimal

#~ departure = [5.4, 1]
#~ destination = [5.9, 3]
#~ print perfectCity(departure, destination)
#~ print '2.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [5.9, 3]
#~ destination = [5.4, 1]
#~ print perfectCity(departure, destination)
#~ print '2.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [5.4, 3]
#~ destination = [5.9, 1]
#~ print perfectCity(departure, destination)
#~ print '2.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [5.9, 1]
#~ destination = [5.4, 3]
#~ print perfectCity(departure, destination)
#~ print '2.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ # When both Y's are decimal

#~ departure = [1, 5.4]
#~ destination = [3, 5.9]
#~ print perfectCity(departure, destination)
#~ print '2.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [3, 5.4]
#~ destination = [1, 5.9]
#~ print perfectCity(departure, destination)
#~ print '2.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [1, 5.9]
#~ destination = [3, 5.4]
#~ print perfectCity(departure, destination)
#~ print '2.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [3, 5.9]
#~ destination = [1, 5.4]
#~ print perfectCity(departure, destination)
#~ print '2.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'







#~ # TEST: Check all possible directions in the same case. Update the decimal point to 0 rather than 1

#~ # When both X's are decimal

#~ departure = [5.2, 0]
#~ destination = [5.5, 1]
#~ print perfectCity(departure, destination)
#~ print '1.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [5.5, 0]
#~ destination = [5.2, 1]
#~ print perfectCity(departure, destination)
#~ print '1.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [5.2, 1]
#~ destination = [5.5, 0]
#~ print perfectCity(departure, destination)
#~ print '1.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [5.5, 1]
#~ destination = [5.2, 0]
#~ print perfectCity(departure, destination)
#~ print '1.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'

#~ # When both Y's are decimal

#~ departure = [0, 5.2]
#~ destination = [1, 5.5]
#~ print perfectCity(departure, destination)
#~ print '1.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [1, 5.5]
#~ destination = [0, 5.2]
#~ print perfectCity(departure, destination)
#~ print '1.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [0, 5.5]
#~ destination = [1, 5.2]
#~ print perfectCity(departure, destination)
#~ print '1.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [1, 5.2]
#~ destination = [0, 5.5]
#~ print perfectCity(departure, destination)
#~ print '1.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'






#~ # TEST: Check another example same to test #1. Update the decimal point to 1

#~ departure = [0.4, 0]
#~ destination = [0.7, 1]
#~ print perfectCity(departure, destination)
#~ print '1.9'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [0.7, 0]
#~ destination = [0.4, 1]
#~ print perfectCity(departure, destination)
#~ print '1.9'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'






#~ # TEST: Check zigzag option

#~ departure = [0.4, 0]
#~ destination = [2.9, 1]
#~ print perfectCity(departure, destination)
#~ print '3.5'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'






#~ # TEST: Another test cases

#~ departure = [2, 1]
#~ destination = [1, 6]
#~ print perfectCity(departure, destination)
#~ print '6.0'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [1, 2]
#~ destination = [6, 1]
#~ print perfectCity(departure, destination)
#~ print '6.0'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [0.4, 1]
#~ destination = [0.9, 3]
#~ print perfectCity(departure, destination)
#~ print '2.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ # WRONG
#~ departure = [1, 0.4]
#~ destination = [3, 0.9]
#~ print perfectCity(departure, destination)
#~ print '2.7'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [0, 0]
#~ destination = [4.7, 9.9]
#~ print perfectCity(departure, destination)
#~ print '14.6'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [0.5,1.5]
#~ destination = [1.5,2.5]
#~ print perfectCity(departure, destination)
#~ print '2.0'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [0.5,1]
#~ destination = [1,2.5]
#~ print perfectCity(departure, destination)
#~ print '2.0'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = []
#~ destination = []
#~ print perfectCity(departure, destination)
#~ print '0.0'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [7, 2.3]
#~ destination = [7, 2.3]
#~ print perfectCity(departure, destination)
#~ print '0.0'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [0.2, 1]
#~ destination = [0.8, 2]
#~ print perfectCity(departure, destination)
#~ print '2.0'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [1, 0.2]
#~ destination = [2, 0.8]
#~ print perfectCity(departure, destination)
#~ print '2.0'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [0.2, 1]
#~ destination = [0.8, 1]
#~ print perfectCity(departure, destination)
#~ print '0.6'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [1, 0.2]
#~ destination = [1, 0.8]
#~ print perfectCity(departure, destination)
#~ print '0.6'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [5, 3.6]
#~ destination = [1, 2.2]
#~ print perfectCity(departure, destination)
#~ print '5.4'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'


#~ departure = [5, 3.6]
#~ destination = [1, 4.2]
#~ print perfectCity(departure, destination)
#~ print '4.6'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n'
