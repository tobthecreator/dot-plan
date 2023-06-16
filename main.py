from line import CreateLine
import plan
import plan2
import sys
from router import Router

# def LoadCliConfig()
# def LoadProjectConfig() # checks to see if there is a plan folder here

def main():
	print("Hello World from python!")

	def getRouterArgs():
		def extractSysArg(a):
			return a if (a != "") else None

		command = sys.argv[1]
		arg2 = extractSysArg(sys.argv[2])
		arg3 = extractSysArg(sys.argv[3])

		return (command, (arg2, arg3))

	cmd, args = getRouterArgs()
	Router(cmd, args)
	

	# print("{} {}".format(command, args))
	"""
 	Structure I'm going with here is:
	(
		type,
		text,
		tags
		timestamp,
	)
 	"""
	
	tests = [
		("!", ".plan cli tool"),
		("!", "programming language for modelling cash flow"),
		("?", "I wonder what they call those tools where you generate code from some template?"),
		("*", "figure out a LISP project"),
		("*", "download COD for father's day"),
		("n", "House of Leaves is a spooky book"),
		("+", "setup a CLI in replit"),
		("-", "i've forgotten most of python"),
	]

	# main could just be the place for setting up configs and such, and then we outsource everything to the CLI
	# then the CLI could call public plan functions itself, that seems easiest

	# use a map later
	
	# for t, txt in tests:
	# 	lines = CreateLine(t, txt)

	# plan.OpenPlan()

	# readCmds = ["2 days ago", "today", "yesterday", "2022-01-01", "01-01-2022", "-3m3w3d", "-72m2w4d", "monday", "last monday", "-1d", "2023-06-16"]

	# for cmd in readCmds:
	# 	print("\n\n")
	# 	print("{}: {}".format(cmd, plan2.ReadPlan(cmd)))
	# 	print("\n\n")

	# next we're going to want to create a file, or update an existing one

	# then read all of these lines into it, and we'll just act like each command line run is a single update


if __name__ == "__main__":
    main()


