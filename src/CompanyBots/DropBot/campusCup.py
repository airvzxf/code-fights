#!/bin/python

def campusCup(emails):

	if len(emails) < 2 and len(emails) > 40:
		return False

	emailsInfo = {}
	pointsPerEmail = 20

	for email in emails:
		
		if len(email) < 5 and len(email) > 20:
				return False

		emailDomain = getDomain(email)

		if  not emailsInfo.has_key(emailDomain):
			emailsInfo[emailDomain] = {}
			emailsInfo[emailDomain]['count'] = 0
			emailsInfo[emailDomain]['points'] = 0
			emailsInfo[emailDomain]['pointsMoreThan'] = 0

		emailsInfo[emailDomain]['count'] += 1
		emailsInfo[emailDomain]['points'] += pointsPerEmail

		points = emailsInfo[emailDomain]['points']
		additionalGBs = 0

		if points >= 500:
			additionalGBs = 25
		elif points >= 300:
			additionalGBs = 15
		elif points >= 200:
			additionalGBs = 8
		elif points >= 100:
			additionalGBs = 3
		
		emailsInfo[emailDomain]['pointsMoreThan'] = additionalGBs

	emailsByPointsMoreThan = createDictionaryPerPoints(emailsInfo)
	emailsList = convertEmailsByPointsToList(emailsByPointsMoreThan)

	return emailsList





def getDomain(email):
	domain = email.split("@") 
	return domain[1]





def createDictionaryPerPoints(emailsInfo):
	
	emailsByPointsMoreThan = {}

	for emailDomain in emailsInfo:

		points = emailsInfo[emailDomain]['pointsMoreThan']

		if  not emailsByPointsMoreThan.has_key(points):
			emailsByPointsMoreThan[points] = []

		emailsByPointsMoreThan[points].append(emailDomain)
		emailsByPointsMoreThan[points].sort(key=len, reverse=False)

	
	return emailsByPointsMoreThan





def convertEmailsByPointsToList(emailsInfo):
	
	emailList = []
	keylist = emailsInfo.keys()
	keylist.sort(reverse=True)

	for key in keylist:
		emailList += emailsInfo[key]
	return emailList



emails = ["john.doe@mit.edu", 
"admin@rain.ifmo.ru", 
"noname@mit.edu"]


emails = [
 "a@rain.ifmo.ru", 
 "b@rain.ifmo.ru", 
 "c@rain.ifmo.ru", 
 "d@rain.ifmo.ru", 
 "e@rain.ifmo.ru", 
 "f@rain.ifmo.ru", 
 "g@rain.ifmo.ru", 
 "h@rain.ifmo.ru", 
 "i@rain.ifmo.ru", 
 "j@rain.ifmo.ru", 
 "k@rain.ifmo.ru", 
 "l@rain.ifmo.ru", 
 "m@rain.ifmo.ru", 
 "n@rain.ifmo.ru", 
 "o@rain.ifmo.ru", 
 "p@rain.ifmo.ru", 
 "q@rain.ifmo.ru", 
 "r@rain.ifmo.ru", 
 "s@rain.ifmo.ru", 
 "t@rain.ifmo.ru", 
 "u@rain.ifmo.ru", 
 "v@rain.ifmo.ru", 
 "w@rain.ifmo.ru", 
 "x@rain.ifmo.ru", 
 "y@rain.ifmo.ru", 
 "a@mit.edu.ru", 
 "b@mit.edu.ru", 
 "c@mit.edu.ru", 
 "d@mit.edu.ru", 
 "e@mit.edu.ru", 
 "f@mit.edu.ru", 
 "g@mit.edu.ru", 
 "h@mit.edu.ru", 
 "i@mit.edu.ru", 
 "j@mit.edu.ru", 
 "k@mit.edu.ru", 
 "l@mit.edu.ru", 
 "m@mit.edu.ru", 
 "n@mit.edu.ru", 
 "o@mit.edu.ru"]


emails = ["a@rain.ifmo.ru", 
 "b@rain.ifmo.ru", 
 "c@rain.ifmo.ru", 
 "d@rain.ifmo.ru", 
 "e@rain.ifmo.ru", 
 "noname@mit.edu"]
 
print 'emails: ', emails

print campusCup(emails)
