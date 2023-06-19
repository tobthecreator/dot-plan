import glob, os
import re
from datetime import date, timedelta
from functools import reduce
from line import CreateLine

# TODO: update this to use project configs tomorrow
def buildPlanFolderPath():
	return os.getcwd() + '/.plan'

def planFolderExists():
	return os.path.exists(buildPlanFolderPath())

# TODO, let's get all of the file stuff into it's own module
def fileExists(filename):
		return os.path.isfile(filename)

def buildFilename(dateStr):
		return "{}/{}.txt".format(buildPlanFolderPath(), dateStr)

# TODO this will need updated to actually only pull .plan files eventually
def getFilenamesFromPath(dir):
	for _, _, filenames in os.walk(dir):
		return filenames

def ListPlans(args):
	if not planFolderExists():
		print("No .plan folder in this current directory")
		return 1

	for filename in getFilenamesFromPath(buildPlanFolderPath()):
		print(filename)

def evaluateDateFromInput(query):
		def todayMinusDays(numDays):
			today = date.today()
			prev = timedelta(days=numDays)

			return (today - prev).strftime("%Y-%m-%d")

		def regexLambda(p):
			return lambda p, q: re.match(p, q)

		def getXDaysAgo(q):
			rNum = int(re.match(r"^(\d+)", q).group(0))
			rRange = re.search(r"(day|week|month|year)", q).group(0)

			scalars = {
				"day": 1,
				"week": 7,
				"month": 30,
				"year": 365
			}

			scalar = scalars[rRange]
			numDays = rNum * scalar
			
			return todayMinusDays(numDays)
		
		def getXDaysAgoShorthand(q):
			matches = re.findall(r"\d+[mwd]", q)
			scalars = {
				"d": 1,
				"w": 7,
				"m": 30
			}
				
			scaleAndSum = lambda sum, match: sum + int(match[:-1]) * scalars[match[-1]]
			numDays = reduce(scaleAndSum, matches, 0)
			
			return todayMinusDays(numDays)

		def getDateString(q):
			x = q.split("-")

			if (len(x[0]) == 4):
				return q

			return "{}-{}-{}".format(x[2], x[1], x[0])
			
		def getNearestWeekday(q):
			match = re.search(rDayOfWeek, q)

			extractedDay = q[match.start():match.end()]
			print(extractedDay)
			
			referenceDate = date.today() if ("last" not in q) else (date.today() - timedelta(days=7))
			referenceWeekday = referenceDate.weekday()
			daysOfWeek = [
				("monday", "m"),
				("tuesday", "t"),
				("wednesday", "w"),
				("thursday", "r"),
				("friday", "f"),
				("saturday", "s"),
				("sunday", "u")
			]

			targetWeekday = next((d for d in daysOfWeek if d[0] == extractedDay or d[1] == extractedDay), 'monday')
			targetWeekdayIndex = daysOfWeek.index(targetWeekday)

			if referenceWeekday == targetWeekdayIndex:
				nearest_day = referenceDate - timedelta(weeks=1)
			elif referenceWeekday > targetWeekdayIndex:
				difference = referenceWeekday - targetWeekdayIndex
				nearest_day = referenceDate - timedelta(days=difference)
			else:
				difference = targetWeekdayIndex - referenceWeekday
				nearest_day = referenceDate - timedelta(days=difference + 7)

			return nearest_day.strftime("%Y-%m-%d")
		

		cases = {
			r"^today$": lambda q: todayMinusDays(0),
			r"^yesterday$": lambda q: todayMinusDays(1), 
			r"^(\d+)\s+(day|week|month|year)s?\s+ago$": getXDaysAgo,
			r"^-\d+[mwd](\d+[mwd])*": getXDaysAgoShorthand,
			r"^(?:(\d{4})-\d{2}-\d{2}|\d{2}-\d{2}-(\d{4}))$": getDateString,
			r"\b(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday|m|t|w|r|f|s|u)\b": getNearestWeekday
		}

		q = query[0].lower() if ((len(query) != 0) and (query[0] not in ["", None])) else "today"

		for pattern, procedure in cases.items():
			if re.search(pattern, q):
				return procedure(q)

		return 1

	
# TODO this could potentially become "accessFiles" and take a list of filenames it iterates over
def accessFile(filename, fileOperationProc, fileDoesNotExistProc):
	if not fileExists(filename):
		returnCode = fileDoesNotExistProc(filename)
		
		if (returnCode not in [0, None]):
			return
		
	
	fileOperationProc(filename)

def ifFileDoesNotExist(_):
	print("Error: that file does not exist")
	return 1	

def ReadPlan(args):
	# TODO: "def findNearest" that scans for a recent date
	def readFile(filename):
		print("\n\n")
		print("reading {}:\n".format(filename))
		with open(filename, "r") as file:
			contents = file.read()
			print(contents)
		print("\n\n")

	

	targetDate = evaluateDateFromInput(args)
	if targetDate == 1:
		return targetDate

	filename = buildFilename(targetDate)

	accessFile(
		filename, 
		readFile, 
		ifFileDoesNotExist
	)
	return 0

def SearchPlans(args):
	print("search plans!")

def UpsertPlan(args):
	def createPlan(filename):
		formattedDate = date.today().strftime("%B %d, %Y")
		headerText = ".plan for {}".format(formattedDate)
		headerDashes = "-"*len(headerText)
		header = "{}\n{}\n{}\n".format(headerDashes, headerText, headerDashes)

		with open(filename, "w") as f:
			f.write(header)

		return 0
	
	def updatePlan(filename, updates):
		with open(filename, "a") as f:
			for update in updates:
				f.write(update)
			

	def parseArgPairs(args):
		return list(zip(args[::2], args[1::2]))

	today = date.today().strftime("%Y-%m-%d")
	filename = buildFilename(today)
	
	pairs = parseArgPairs(args)
	updates = map(lambda t: CreateLine(t[0], t[1]), pairs)

	accessFile(
		filename, 
		lambda f: updatePlan(f, updates),
		createPlan
	)

	return 0

def DeletePlan(args):
	def deleteFile(filename): 
		print("deleting {}".format(filename))
		os.remove(filename)



	targetDate = evaluateDateFromInput(args)
	if targetDate == 1:
		return targetDate
	
	filename = buildFilename(targetDate)

	accessFile(
		filename, 
		deleteFile, 
		ifFileDoesNotExist
	)