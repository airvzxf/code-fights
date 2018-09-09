def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
	
	#~ print 'ride_time: ', ride_time
	#~ print 'cost_per_minute: ', cost_per_minute
	#~ print 'ride_distance: ', ride_distance
	#~ print 'cost_per_mile: ', cost_per_mile
	#~ print '\n'

	fareEstimator = []
	
	for i in range(len(cost_per_minute)):
		fareEstimator.append( round((ride_time * cost_per_minute[i]) + (ride_distance * cost_per_mile[i]), 2) )

		if fareEstimator[i].is_integer():
			fareEstimator[i] = int(fareEstimator[i])

	return fareEstimator
		


#~ ride_time = 30
#~ ride_distance = 7
#~ cost_per_minute = [0.2, 0.35, 0.4, 0.45]
#~ cost_per_mile = [1.1, 1.8, 2.3, 3.5]
#~ print fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile)
#~ print '[13.7, 23.1, 28.1, 38]'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n\n\n\n'



#~ ride_time = 15
#~ ride_distance = 9
#~ cost_per_minute = [0.2, 0.34, 0.35, 0.45, 1]
#~ cost_per_mile = [1.1, 1.8, 1.9, 1.7, 5]
#~ print fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile)
#~ print '[12.9, 21.3, 22.35, 22.05, 60]'
#~ print '-------------------------------------------------------------------'
#~ print '\n\n\n\n\n'
