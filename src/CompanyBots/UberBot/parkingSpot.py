# PENDING: To check in the code fighters.

def parkingSpot(carDimensions, parkingLot, luckySpot):

	lengthCar, widthCar = carDimensions
	numRows = len(parkingLot)
	numCols = len(parkingLot[0])

	#~ print 'carDimensions: ', carDimensions
	#~ print 'parkingLot: ', parkingLot
	#~ print 'luckySpot: ', luckySpot
	#~ print ''

	print 'widthCar: ', widthCar
	print 'lengthCar: ', lengthCar
	#~ print ''


	#~ print 'Check the width space in parking lot.'
	#~ print 'numRows: ', numRows
	#~ print 'numCols: ', numCols
	#~ print ''

	if isNotLuckySpotAvailable(parkingLot, luckySpot):
		print 'isNotLuckySpotAvailable. Yes, it is NOT Available'
		return False
	
	widthSpaceInParkingLot = {'left':[],'top':[],'right':[],'bottom':[]}
	
	luckySpotSumFirst = luckySpot[2] - luckySpot[0] + 1
	luckySpotSumSecond = luckySpot[3] - luckySpot[1] + 1
	#~ print 'luckySpotSumFirst: ', luckySpotSumFirst
	#~ print 'luckySpotSumSecond: ', luckySpotSumSecond

	if luckySpotSumFirst == carDimensions[0] and luckySpotSumSecond == carDimensions[1]:
		#~ print '*** First: Vertical'
		widthSpaceInParkingLot = getVerticalSpaceAvailables(parkingLot, widthSpaceInParkingLot, numRows, numCols, widthCar, lengthCar)
	elif luckySpotSumFirst == carDimensions[1] and luckySpotSumSecond == carDimensions[0]:
		#~ print '*** Second: Horizontal'
		widthSpaceInParkingLot = getHorizontalSpaceAvailables(parkingLot, widthSpaceInParkingLot, numRows, numCols, widthCar, lengthCar)

	#~ widthSpaceInParkingLot = getHorizontalSpaceAvailables(parkingLot, widthSpaceInParkingLot, numRows, numCols, widthCar, lengthCar)
	#~ widthSpaceInParkingLot = getVerticalSpaceAvailables(parkingLot, widthSpaceInParkingLot, numRows, numCols, widthCar, lengthCar)
	
	print 'FINAL: widthSpaceInParkingLot: ', widthSpaceInParkingLot
	#~ print 'widthCar: ', widthCar
	#~ print 'lengthCar: ', lengthCar

	
	for key in widthSpaceInParkingLot:
		#~ print 'key: ', key
		for spaces in widthSpaceInParkingLot[key]:
			#~ print 'spaces: ', spaces
			#~ print 'spaces[2]: ', spaces[2]
			if lengthCar <= spaces[2]:
				return True

	return False



def isNotLuckySpotAvailable(parkingLot, luckySpot):
	
	if sum(luckySpot[0:2]) < sum(luckySpot[2:4]):
		#~ print 'First point is lower'
		firstCoord = luckySpot[0:2]
		secondCoord = luckySpot[2:4]
	else:
		#~ print 'Second point is lower'
		firstCoord = luckySpot[2:4]
		secondCoord = luckySpot[0:2]
	
	#~ print 'firstCoord: ', firstCoord
	#~ print 'secondCoord: ', secondCoord
	
	for x in range(firstCoord[0], secondCoord[0]+1):
		#~ print 'x: ', x
		for y in range(firstCoord[1], secondCoord[1]+1):
			#~ print 'y: ', y
			#~ print 'parkingLot[x][y]: ', parkingLot[x][y]
			if parkingLot[x][y] == 1:
				return True
	#~ print '\n'
	return False




def getHorizontalSpaceAvailables(parkingLot, widthSpaceInParkingLot, numRows, numCols, widthCar, lengthCar): 

	#~ print 'Get the coords to the spaces availables in horizontal'
	#~ print '--------------------------------------'
	
	if lengthCar > numCols:
		print '*** lengthCar > numCols'
		print 'numCols: ', numCols
		print 'lengthCar: ', lengthCar
		return widthSpaceInParkingLot

	horizontalMode = [['left',0], ['right', numCols - 1]]

	for h in horizontalMode:

		chekingSide, chekingRow = h
		#~ print 'chekingSide: ', chekingSide
		#~ print 'chekingRow: ', chekingRow
		#~ print ''

		for n in range(numRows):
			#~ print 'parkingLot[n][chekingRow]: ', parkingLot[n][chekingRow]
			#~ print 'n: ', n
			#~ print 'chekingRow: ', chekingRow

			if parkingLot[n][chekingRow] == 0:
				#~ print 'numRows - n = ', (numRows - n)
				#~ print 'widthCar: ', widthCar

				if (numRows - n) >= widthCar:
					isAvailableSize = True

					for m in range(n, n+widthCar):

						if parkingLot[m][chekingRow] == 1:
							isAvailableSize = False
							break
						#~ print 'parkingLot[m][0]: ', parkingLot[m][chekingRow]

					if isAvailableSize:
						#~ print 'Successful: The width car is on parking lot.'
						widthSpaceInParkingLot[chekingSide].append([n,chekingRow,0])

			#~ print ''
		#~ print '\n-------------\n'

		#~ print 'widthSpaceInParkingLot: ', widthSpaceInParkingLot
		#~ print '\n------------- -------------\n'


		# Count the spaces availables in horizontal mode checking the lenght of car

		#~ print 'Count the spaces availables in horizontal'
		#~ print '--------------------------------------'

		
		for i in range(len(widthSpaceInParkingLot[chekingSide])):

			#~ print 'widthSpaceInParkingLot[chekingSide][i]: ', widthSpaceInParkingLot[chekingSide][i]
			x, y, size = widthSpaceInParkingLot[chekingSide][i]
			isAvailableSize = True
			sizeCount = 0


			for n in range(numCols):

				if isAvailableSize == False:
					break

				#~ print 'n: ', n

				for w in range(widthCar):
					#~ print 'w: ', w
					if chekingSide == 'left':
						freeSpace = parkingLot[x+w][y+n]
					elif chekingSide == 'right':
						freeSpace = parkingLot[x+w][y-n]

					if freeSpace == 1:
						isAvailableSize = False
						break

				if isAvailableSize:
					sizeCount += 1
					widthSpaceInParkingLot[chekingSide][i][2] = sizeCount

				#~ print ''

			#~ print ''

		#~ print ''

		#~ print 'widthSpaceInParkingLot: ', widthSpaceInParkingLot
		#~ print '\n------------- -------------\n'
	#~ print '\n------------- ------------- -------------\n'
	return widthSpaceInParkingLot






def getVerticalSpaceAvailables(parkingLot, widthSpaceInParkingLot, numRows, numCols, widthCar, lengthCar): 

	#~ print 'Get the coords to the spaces availables in vertical'
	#~ print '--------------------------------------'

	if lengthCar > numRows:
		print '*** lengthCar > numRows'
		print 'numRows: ', numRows
		print 'lengthCar: ', lengthCar
		return widthSpaceInParkingLot

	verticalMode = [['top',0], ['bottom', numRows - 1]]

	for v in verticalMode:

		chekingSide, chekingCol = v
		#~ print 'chekingSide: ', chekingSide
		#~ print 'chekingCol: ', chekingCol
		#~ print ''

		for n in range(numCols):
			#~ print 'parkingLot[chekingCol][n]: ', parkingLot[chekingCol][n]
			#~ print 'n: ', n
			#~ print 'chekingCol: ', chekingCol

			if parkingLot[chekingCol][n] == 0:
				#~ print 'numCols - n = ', (numCols - n)
				#~ print 'widthCar: ', widthCar

				if (numCols - n) >= widthCar:
					isAvailableSize = True

					for m in range(n, n+widthCar):

						if parkingLot[chekingCol][m] == 1:
							isAvailableSize = False
							break
						#~ print 'parkingLot[chekingCol][m]: ', parkingLot[chekingCol][m]

					if isAvailableSize:
						#~ print 'Successful: The width car is on parking lot.'
						widthSpaceInParkingLot[chekingSide].append([chekingCol,n,0])

			#~ print ''
		#~ print '\n-------------\n'

		#~ print 'widthSpaceInParkingLot: ', widthSpaceInParkingLot
		#~ print '\n------------- -------------\n'


		# Count the spaces availables in vertical mode checking the lenght of car

		#~ print 'Count the spaces availables in vertical'
		#~ print '--------------------------------------'

		for i in range(len(widthSpaceInParkingLot[chekingSide])):

			#~ print 'widthSpaceInParkingLot[chekingSide][i]: ', widthSpaceInParkingLot[chekingSide][i]
			x, y, size = widthSpaceInParkingLot[chekingSide][i]
			isAvailableSize = True
			sizeCount = 0


			#~ print 'numRows: ', numRows
			for n in range(numRows):

				if isAvailableSize == False:
					break

				
				#~ print 'x: ', x
				#~ print 'y: ', y
				#~ print 'n: ', n

				for w in range(widthCar):
					#~ print 'w: ', w

					if chekingSide == 'top':
						#~ print 'parkingLot[x+n][y+w]: ', parkingLot[x+n][y+w]
						#~ print '[x+n]: ', x+n
						#~ print '[y+w]: ', y+w
						freeSpace = parkingLot[x+n][y+w]
					elif chekingSide == 'bottom':
						#~ print 'parkingLot[x-w][y+n]: ', parkingLot[x-n][y+w]
						#~ print '[x-n]: ', x-n
						#~ print '[y+w]: ', y+w
						freeSpace = parkingLot[x-n][y+w]

					if freeSpace == 1:
						isAvailableSize = False
						break

				if isAvailableSize:
					sizeCount += 1
					widthSpaceInParkingLot[chekingSide][i][2] = sizeCount

				#~ print ''

			#~ print ''

		#~ print ''

		#~ print 'widthSpaceInParkingLot: ', widthSpaceInParkingLot
		#~ print '\n------------- -------------\n'
	#~ print '\n------------- ------------- -------------\n'
	return widthSpaceInParkingLot









# TEST = Originals test cases

print '# No. 1'
carDimensions = [3, 2]
parkingLot = [
[1,0,1,0,1,0],
[0,0,0,0,1,0],
[0,0,0,0,0,1],
[1,0,1,1,1,1]]
luckySpot = [1, 1, 2, 3]
print parkingSpot(carDimensions, parkingLot, luckySpot)
print 'true'
print '-------------------------------------------------------------------'
print '\n\n'


print '# No. 2'
carDimensions = [3, 2]
parkingLot = [
[1,0,1,0,1,0],
[1,0,0,0,1,0],
[0,0,0,0,0,1],
[1,0,0,0,1,1]]
luckySpot = [1, 1, 2, 3]
print parkingSpot(carDimensions, parkingLot, luckySpot)
print 'false'
print '-------------------------------------------------------------------'
print '\n\n'


print '# No. 3'
carDimensions = [4, 1]
parkingLot = [
[1,0,1,0,1,0],
[1,0,0,0,1,0],
[0,0,0,0,0,1],
[1,0,0,0,1,1]]
luckySpot = [0, 3, 3, 3]
print parkingSpot(carDimensions, parkingLot, luckySpot)
print 'true'
print '-------------------------------------------------------------------'
print '\n\n'


print '# No. 4'
carDimensions = [2, 1]
parkingLot = [
[1,0,1],
[1,0,1],
[1,1,1]]
luckySpot = [0, 1, 1, 1]
print parkingSpot(carDimensions, parkingLot, luckySpot)
print 'true'
print '-------------------------------------------------------------------'
print '\n\n'


print '# No. 5'
carDimensions = [4, 2]
parkingLot = [
[0,0,0,1],
[0,0,0,0],
[0,0,1,1]]
luckySpot = [0, 0, 1, 3]
print parkingSpot(carDimensions, parkingLot, luckySpot)
print 'false'
print '-------------------------------------------------------------------'
print '\n\n'


print '# No. 6'
carDimensions = [7, 2]
parkingLot = [
[0,1,0],
[0,0,0],
[0,0,0],
[0,0,0],
[0,0,0],
[0,0,0],
[0,0,0],
[0,0,0]]
luckySpot = [1, 0, 7, 1]
print parkingSpot(carDimensions, parkingLot, luckySpot)
print 'true'
print '-------------------------------------------------------------------'
print '\n\n'


print '# No. 7'
carDimensions = [5, 3]
parkingLot = [
[1,1,1,1,1,0,1,1,1,1],
[0,1,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0,1,0],
[0,0,1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0]]
luckySpot = [1, 3, 5, 5]
print parkingSpot(carDimensions, parkingLot, luckySpot)
print 'false'
print '-------------------------------------------------------------------'
print '\n\n'


print '# No. 8'
carDimensions = [2, 1]
parkingLot = [
[1,0,1],
[1,0,1],
[1,1,1]]
luckySpot = [1, 1, 2, 1]
print parkingSpot(carDimensions, parkingLot, luckySpot)
print 'false'
print '-------------------------------------------------------------------'
print '\n\n'


print '# No. 9'
carDimensions = [2, 1]
parkingLot = [
[1,1,1],
[1,0,1],
[1,0,1]]
luckySpot = [0, 1, 1, 1]
print parkingSpot(carDimensions, parkingLot, luckySpot)
print 'false'
print '-------------------------------------------------------------------'
print '\n\n'


print '# No. 10'
carDimensions = [2, 1]
parkingLot = [
[1,1,1,1],
[1,0,0,0],
[1,0,1,0]]
luckySpot = [2, 1, 2, 2]
print parkingSpot(carDimensions, parkingLot, luckySpot)
print 'false'
print '-------------------------------------------------------------------'
print '\n\n'


print '# No. 11'
carDimensions = [2, 1]
parkingLot = [
[1,1,1,1], 
[1,0,0,0], 
[1,0,1,0]]
luckySpot = [1, 2, 1, 3]
print parkingSpot(carDimensions, parkingLot, luckySpot)
print 'true'
print '-------------------------------------------------------------------'
print '\n\n'


print '# No. 12'
carDimensions = [7, 2]
parkingLot = [
[0,0,0,0,0,0,0,0], 
[1,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0]]
luckySpot = [1, 1, 2, 7]
print parkingSpot(carDimensions, parkingLot, luckySpot)
print 'true'
print '-------------------------------------------------------------------'
print '\n\n'
