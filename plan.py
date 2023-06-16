from random import randint
from datetime import date
import os

def UpsertPlan(planConfig):
	OpenOrCreateFile(planConfig)

# okay so a user hits me with a command in the CLI
# to remove friction, we'll just create a file if they don't have it
# we'll let the know that happened
# otherwise we'll just update the file

# what does plan config look like?
# maybe something like
# project name for now? and this is where we can hide all of the other goodies later
# can edit this from the CLI and hide it in the bin? or maybe it's put in the plan folder
# i think plan folder probably makes more sense, since it's the project settings
# then we can have CLI settings that ARE stored in the bin

# feels like the plan is the element we're interacting with via the API, not lines really
# although we'll be able to add a line/lines from the CLI, those by default are editing today's plan

# for now i want to keep the structure really simple, so we'll just assume that there are plan files in the same directory that the CLI is running in. I think it'd be cooler if the CLI searching for a .plan folder or something, or maybe just knew where projects were globally and could edit them.  Either way, a .plan folder with a bunch of files in seems right for clutter purposes.





def OpenOrCreateFile(planConfig):
	def buildFilename():
		dateStr = date.today().strftime("%Y-%m-%d")
		o = "{}.txt".format(dateStr)

		return o


	file_name = buildFilename()

	if os.path.isfile(file_name):
		# File exists, so open it
		with open(file_name, "r") as file:
			# Perform operations with the file
			# For example, read its contents
			contents = file.read()
			print("File contents:", contents)
				
	else:
		# File doesn't exist, so create it and write to it
		with open(file_name, "w") as file:
			# Write to the file
			file.write("This is a new file.")

		print("File created and written successfully.")
	



def openFile(filename):
		return open(filename, "w+")

def CreatePlan(filename):
	# create the plan file and initialize it
	pF = openFile(filename)

	pF.write("Tyler O'Briant Plan File for today")

	return pF

def OpenPlan():
	# plan name for now is plan_date.txt
	def buildFilename():
		dateStr = date.today().strftime("%Y-%m-%d")
		o = "plan_{}.txt".format(dateStr)

		return o

	# we're assuming it's in this direct path with us right now, not at some config location or folder
	def fileExists(filename):
		return os.path.isfile(filename)

	

	# okay some interesting notes is that the different file write modes might actually be useful here.

	# there is read-only, append only, write, write AND read
	# so we may just not care about redundancy as much and treat this like a normal API yah know

	# have a router, have a service
	filename = buildFilename()

	pF = openFile(filename) if (fileExists(filename)) else CreatePlan(filename)

	ReadPlan(pF)
	
	pF.close()

	# in here we're going to look to see if we have a plan file for today
	# if we do, we'll return it
	# if we do not, we'll create it, initialize it, and then return it

#def UpdatePlan():
	# update plan file
	# will take in 

#def DeletePlan():
	# delete the file

def ReadPlan(file):
	# will simply read the plan file
	for line in file:
		print(line)

#def FormatPlan():
	# will apply formatting and overwrite the plan file's current formatting



