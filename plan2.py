# okay in this one we're just going to make each function responsible for 
# managing it's own file access.

import glob, os
import re
from datetime import date, timedelta
from functools import reduce

PLANS_DIR = '{}/plans'.format(os.getcwd())

def fileExists(filename):
		return os.path.isfile(filename)

def buildFilename(dateStr):
		return "plan_{}.txt".format(dateStr)

def getAllPlanFilenames():
	# little worried what happens when there are more
	# than one root and dir arg here, the _
	# can always fix later, it works now
	for _, _, filenames in os.walk(PLANS_DIR):
		return filenames


def ListPlans():
	print("list plans!")
	# print(os.getcwd())
	
	for filename in getAllPlanFilenames():
		print(filename) # some of this could probably be a bash command instead
			# in fact, couldn't all this be a bash command? lol. we're just editing a text file

def ReadPlan(args):
	query = args[0].lower() if (args[0] != "") else "today"

	def evaluateDateFromInput(q):
		def regexLambda(p):
			return lambda p, q: re.match(p, q)

		rToday = r"^today$"
		fToday = lambda q: date.today().strftime("%Y-%m-%d")
		
		rYesterday = r"^yesterday$"
		fYesterday = lambda q: (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
		
		rXAgo = r"^(\d+)\s+(day|week|month|year)s?\s+ago$"
		def fXAgo(q):
			rNum = int(re.match(r"^(\d+)", q).group(0))
			rRange = re.search(r"(day|week|month|year)", q).group(0)

			scalars = {
				"day": 1,
				"week": 7,
				"month": 30,
				"year": 365
			}

			scalar = scalars[rRange]
			daysAgo = rNum*scalar
			
			return (date.today() - timedelta(days=daysAgo)).strftime("%Y-%m-%d")
		
		rXAgoShorthand = r"^-\d+[mwd](\d+[mwd])*"
		def fXAgoShorthand(q):
			matches = re.findall(r"\d+[mwd]", q)
			scalars = {
				"m": 30, 
				"w": 7, 
				"d": 1
			}
				
			scaleAndSum = lambda sum, match: sum + int(match[:-1]) * scalars[match[-1]]
			daysAgo = reduce(scaleAndSum, matches, 0)
			
			return (date.today() - timedelta(days=daysAgo)).strftime("%Y-%m-%d")

		rDateString = r"^(?:(\d{4})-\d{2}-\d{2}|\d{2}-\d{2}-(\d{4}))$"
		def fDateString(q):
			x = q.split("-")

			if (len(x[0]) == 4):
				return q

			return "{}-{}-{}".format(x[2], x[1], x[0])
			
		rDayOfWeek = r"\b(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday|m|t|w|r|f|s|u)\b"
		def fDayOfWeek(q):
			match = re.search(rDayOfWeek, q)

			extractedDay = q[match.start():match.end()]
			print(extractedDay)
			
			referenceDate = date.today() if ("last" not in q) else (date.today() - timedelta(days=7))
			referenceWeekday = referenceDate.weekday()
			days_of_week = [
				("monday", "m"),
				("tuesday", "t"),
				("wednesday", "w"),
				("thursday", "r"),
				("friday", "f"),
				("saturday", "s"),
				("sunday", "u")
			]

			# print('filter', filter(lambda d: d[0] == q or d[1], days_of_week)[0])
			# print('days_of_week.index()', days_of_week.index(filter(lambda d: d[0] == q or d[1], days_of_week)[0]))

			# next((x for x in array if x % 2 == 0), None)
			target_weekday = next((d for d in days_of_week if d[0] == extractedDay or d[1] == extractedDay), 'monday')
			target_weekday_index = days_of_week.index(target_weekday)

			if referenceWeekday == target_weekday_index:
				nearest_day = referenceDate - timedelta(weeks=1)
			elif referenceWeekday > target_weekday_index:
				difference = referenceWeekday - target_weekday_index
				nearest_day = referenceDate - timedelta(days=difference)
			else:
				difference = target_weekday_index - referenceWeekday
				nearest_day = referenceDate - timedelta(days=difference + 7)

			return nearest_day.strftime("%Y-%m-%d")
		
		cases = [
			(
				rToday, # done
				fToday
			),
			(
				rYesterday, # done
				fYesterday
			),
			(
				rXAgo, # done? -> yes
				fXAgo
			),
			(
				rXAgoShorthand, # done? -> yes
				fXAgoShorthand
			),
			(
				rDateString, # done? -> yes
				fDateString				
			),
			(
				rDayOfWeek, # done? -> yes
				fDayOfWeek
			)
		]

		for pattern, procedure in cases:
			if re.search(pattern, q):
				return procedure(q)

		return "default" # TODO return error

	# for now, if there is nothing at the corresponding date, then we'll just say so
	# eventually I want a "def findNearest" that will give you the option to scan for the nearest date and pull that up

	def readFile(filename):
		print("\n\n")
		print("reading {}:\n".format(filename))
		with open(filename, "r") as file:
			contents = file.read()
			print(contents)
		print("\n\n")

	targetDate = evaluateDateFromInput(query)
	filename = buildFilename(targetDate)
	
	if (fileExists(filename)):
		readFile(buildFilename(targetDate))

	else:
		# throw a real error
		print("hey that doesn't exist!")
	
	return targetDate




def UpsertPlan():
	print("add lines to plan!")

def DeletePlan():
	print("deleting plan!")

