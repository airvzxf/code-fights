#!/bin/python



def fileSyncOrder(files, storageLimit, uploadSpeed, duration):

	#~ print 'fileSyncOrder\n'

	#~ print 'files: ', files
	#~ print 'storageLimit: ', storageLimit
	#~ print 'uploadSpeed: ', uploadSpeed
	#~ print 'duration: ', duration
	#~ print '\n\n'


	files = filesAddIndex(files)
	timeToFinishedSync = files[0][1]
	fileSizeSync = 0


	result = filesSyncRecursive(1, [], timeToFinishedSync, fileSizeSync, files, storageLimit, uploadSpeed, duration)
	
	#~ print '\n\n'
	print 'Last Result in fileSyncOrder'
	print '-----------------------------------'
	print result
	return result





def filesAddIndex(files):

	fileIndex = 0
	# Add indext at the end
	# files[ [Size, StartTime, Index], ]
	for fileIndex in range(len(files)):
		files[fileIndex].append(fileIndex)

	files = sorted(files, key=lambda x: (x[1], x[0]))

	return files





def filesDelteOversizeAndOvertime(files, timeToFinishedSync, fileSizeSync, storageLimit, uploadSpeed, duration):

	#~ print ''
	#~ print 'filesDelteOversizeAndOvertime:'
	for f in files:

		maxTimeInFile = (f[0] / uploadSpeed) + timeToFinishedSync
		#~ print 'IF maxTimeInFile: ', maxTimeInFile, '>', 'duration: ', duration
		if maxTimeInFile > duration:
			#~ print 'Delete file: ', f
			files.remove(f)

		maxSizeInFile = f[0] + fileSizeSync
		#~ print 'IF maxSizeInFile: ', maxSizeInFile, '>', 'storageLimit: ', storageLimit
		if maxSizeInFile > storageLimit:
			#~ print 'Delete file: ', f
			files.remove(f)

	#~ print ''

	return files





def filesSyncRecursive(depth, result, timeToFinishedSync, fileSizeSync, files, storageLimit, uploadSpeed, duration):

	#~ print 'fileSyncRecursve'
	#~ print '-----------------------------------'

	files = sorted(files, key=lambda x: (x[1]))

	#~ print 'result: ', result
	#~ print 'storageLimit: ', storageLimit
	#~ print 'uploadSpeed: ', uploadSpeed
	#~ print 'duration: ', duration
	#~ print 'timeToFinishedSync: ', timeToFinishedSync
	#~ print 'fileSizeSync: ', fileSizeSync
	#~ print 'files: ', files, '\n'


	#~ print 'files Orig: ', files
	files = filesDelteOversizeAndOvertime(files, timeToFinishedSync, fileSizeSync, storageLimit, uploadSpeed, duration)
	#~ print 'files Debg: ', files, '\n'
	
	filesInTimeRange = [x for x in files if x[1] <= timeToFinishedSync]
	filesInTimeRange = sorted(filesInTimeRange, key=lambda x: (x[0]))

	if len(filesInTimeRange) == 0:
		timeToFinishedSync = 0
		filesInTimeRange = sorted(files, key=lambda x: (x[1], x[0]))
	#~ print 'filesInTimeRange: ', filesInTimeRange

	if len(files) == 0:
		#~ print 'Break Not Files'
		return result


	fileSynchronizing = filesInTimeRange[0]
	timeToFinishedSync += (fileSynchronizing[0] / uploadSpeed)
	fileSizeSync += fileSynchronizing[0]
	#~ print 'fileSynchronizing: ', fileSynchronizing
	#~ print 'timeToFinishedSync: ', timeToFinishedSync
	#~ print 'fileSizeSync: ', fileSizeSync


	if timeToFinishedSync > duration:
		#~ print 'Break time enough'
		return result

	if fileSizeSync > storageLimit:
		#~ print 'Break Store Limit enough'
		return result

	result.append(fileSynchronizing[2])
	files.remove(fileSynchronizing)
	#~ print '\n'
	#~ print 'files: ', files
	#~ print 'result: ', result
	#~ print result



	#~ print '\n'
	#~ print 'Just Start the functon again: filesSyncRecursive'
	#~ print '-----------------------------------'
	#~ print '\n\n\n\n'

	filesSynchronized = filesSyncRecursive(depth+1, result, timeToFinishedSync, fileSizeSync, files, storageLimit, uploadSpeed, duration)
	return filesSynchronized





#~ files = [
#~ [10,5],
#~ [10,7],
#~ [8,10],
#~ [2,20]
#~ ]
#~ storageLimit = 20
#~ uploadSpeed = 2
#~ duration = 100

#~ fileSyncOrder(files, storageLimit, uploadSpeed, duration)
#~ print '[0, 2, 3]'
#~ print '\n\n'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n\n\n\n'



#~ files = [
#~ [10,5]
#~ ]
#~ storageLimit = 100
#~ uploadSpeed = 1
#~ duration = 10

#~ fileSyncOrder(files, storageLimit, uploadSpeed, duration)
#~ print '[]'
#~ print '\n\n'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n\n\n\n'



#~ files = [
#~ [20,5],
#~ [10,5],
#~ [30,7]
#~ ]
#~ storageLimit = 100
#~ uploadSpeed=  1
#~ duration = 40

#~ fileSyncOrder(files, storageLimit, uploadSpeed, duration)
#~ print '[1, 0]'
#~ print '\n\n'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n\n\n\n'



#~ files = [
#~ [20,5],
#~ [10,5],
#~ [3,7]
#~ ]
#~ storageLimit = 100
#~ uploadSpeed = 1
#~ duration = 40

#~ fileSyncOrder(files, storageLimit, uploadSpeed, duration)
#~ print '[1, 2, 0]'
#~ print '\n\n'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n\n\n\n'



#~ files = [
#~ [20,5],
#~ [10,5],
#~ [3,7]
#~ ]
#~ storageLimit = 100
#~ uploadSpeed = 1
#~ duration = 4

#~ fileSyncOrder(files, storageLimit, uploadSpeed, duration)
#~ print '[]'
#~ print '\n\n'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n\n\n\n'


#~ files = [
#~ [10,1],
#~ [20,1],
#~ [30,1]
#~ ]
#~ storageLimit = 60
#~ uploadSpeed = 2
#~ duration = 31

#~ fileSyncOrder(files, storageLimit, uploadSpeed, duration)
#~ print '[0, 1, 2]'
#~ print '\n\n'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n\n\n\n'
