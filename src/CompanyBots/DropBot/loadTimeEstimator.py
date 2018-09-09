# Incomplete!
# =(

def loadTimeEstimator(sizes, uploadingStart, V):
	print 'sizes: ', sizes
	print 'uploadingStart: ', uploadingStart
	print 'V: ', V

	if len(sizes) == 0:
		print 'Not any file'
		return sizes

	files = []
	filesTimeResult = []

	for f in range(len(sizes)):
		# files = [Index, FileSize, FileUplodingStart]
		files.append([f, sizes[f], uploadingStart[f]])
		filesTimeResult.append(0)

	print 'files: ', files
	print 'filesTimeResult: ', filesTimeResult
	print ''

	result = fileimeEstimator(files,  V, 0, filesTimeResult)

	return result



def fileimeEstimator(files, uploadSpeed, currentTime, filesTimeResult):

	uploadSpeed = float(uploadSpeed)
	# Creat formula to get the minimun number of time to finish any task
	minCurrentTime = min([(x[2]) for x in files]) #Something like: fileSize / uploadSpedd, the problem is know if some task have concurrency
	currentTime += 1
	

	splitUploadSpeed = 0
	isFilesSizesEquelToZero = True

	print '\n\n\n\n'
	print 'fileimeEstimator:\n'

	print 'minCurrentTime: ', minCurrentTime
	print 'currentTime: ', currentTime

	# If the input Sizes always are sorted by time, this line still commented.
	#~ files = sorted(files, key=lambda x: (x[2], x[1]))

	for f in range(len(files)):
		if files[f][1] > 0 and files[f][2] <= currentTime:
			splitUploadSpeed += 1

	if splitUploadSpeed == 0:
		minFilesTime = min([x[2] for x in files])
		print 'minFilesTime: ', minFilesTime
		print 'splitUploadSpeed is equal than zero, check the next file.\n'
		result = fileimeEstimator(files, uploadSpeed, minFilesTime, filesTimeResult)
		print 'result: ', result
		return result

	print 'splitUploadSpeed: ', splitUploadSpeed

	realUploadSpeed = uploadSpeed / splitUploadSpeed
	print 'realUploadSpeed: ', realUploadSpeed
	print ''


	print 'files: ', files
	print ''



	i = -1
	for f in files[:]:


		i += 1
		print 'f = ', f
		print 'i: ', i

		if f[1] == 0:
			print 'if', f[1], '==', 0
			print 'This files has been uploaded\n'
			continue

		if f[2] > currentTime:
			print 'if', f[2], '>', currentTime
			print 'Time is more than the fist time\n'
			isFilesSizesEquelToZero = False
			continue


		print 'fileTimeDiff: ', (currentTime - f[2])

		print f[1], '- (', realUploadSpeed, '*', (currentTime - f[2]), ')'
		fistFileUplad = f[1] - (realUploadSpeed * (currentTime - f[2]))

		if fistFileUplad <= 0:
			filesTimeResult[f[0]] = currentTime
			files.remove(f)
			i -= 1
			print 'filesTimeResult: ', filesTimeResult
			print 'files: ', files
			print ''
			continue


		files[i][1] = fistFileUplad
		files[i][2] = currentTime
		print 'fistFileUplad: ', fistFileUplad

		print 'files: ', files
		print ''



	print '-------------\n'


	print 'files: ', files
	print 'filesTimeResult: ', filesTimeResult
	print '\n\n'

	if isFilesSizesEquelToZero:
		print 'isFilesSizesEquelToZero == True'
		result = []
		for f in range(len(files)):
			result.append(files[f][2])
		return result

	print 'This recursive method was finished!'
	minFilesTime = min([x[2] for x in files])
	print 'minFilesTime: ', minFilesTime
	result = fileimeEstimator(files, uploadSpeed, minFilesTime, filesTimeResult)
	print 'result: ', result
	return result

	None




sizes = [21, 10, 1, 2, 3]
uploadingStart = [100, 105, 100, 100, 100]
V = 8
print loadTimeEstimator(sizes, uploadingStart, V)
print '[104, 107, 101, 101, 102]'
print '-------------------------------------------------------------------'
print '\n\n\n\n\n'



sizes = [21, 10]
uploadingStart = [100, 105]
V = 2
print loadTimeEstimator(sizes, uploadingStart, V)
print '[116, 115]'
print '-------------------------------------------------------------------'
print '\n\n\n\n\n'



sizes = [20, 10]
uploadingStart = [1, 1]
V = 1
print loadTimeEstimator(sizes, uploadingStart, V)
print '[31, 21]'
print '-------------------------------------------------------------------'
print '\n\n\n\n\n'



sizes = []
uploadingStart = []
V = 100
print loadTimeEstimator(sizes, uploadingStart, V)
print '[]'
print '-------------------------------------------------------------------'
print '\n\n\n\n\n'



sizes = [10]
uploadingStart = [10]
V = 2
print loadTimeEstimator(sizes, uploadingStart, V)
print '[15]'
print '-------------------------------------------------------------------'
print '\n\n\n\n\n'



sizes = [1, 1, 1]
uploadingStart = [2, 2, 2]
V = 3
print loadTimeEstimator(sizes, uploadingStart, V)
print '[3, 3, 3]'
print '-------------------------------------------------------------------'
print '\n\n\n\n\n'



sizes = [1, 1, 1]
uploadingStart = [10, 20, 30]
V = 3
print loadTimeEstimator(sizes, uploadingStart, V)
print '[11, 21, 31]'
print '-------------------------------------------------------------------'
print '\n\n\n\n\n'
