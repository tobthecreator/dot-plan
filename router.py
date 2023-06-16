import plan2

# here we're going to take in all of our CLI commands and parse them out to the right functions

# can make a CMD enum if we care enough

# lots of interesting stuff we can do in here https://learnpython.com/blog/python-match-case-statement/
def Router(cmd, args):
	match (cmd):
		case "r" | "read":
			return plan2.ReadPlan(args)

		case "w" | "write":
			return plan2.UpsertPlan(args)

		case "s" | "search":
			return plan2.SearchPlans(args)

		case "d" | "delete":
			return plan2.DeletePlan(args)

		case "l" | "list":
			return plan2.ListPlans(args)

		case _:
			# throw an error
			print("router!")
		