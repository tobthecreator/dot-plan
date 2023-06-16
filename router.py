import plan2

# here we're going to take in all of our CLI commands and parse them out to the right functions

# can make a CMD enum if we care enough

# lots of interesting stuff we can do in here https://learnpython.com/blog/python-match-case-statement/
def Router(cmd, args):
	match (cmd):
		case "r" | "read":
			plan2.ReadPlan(args)

		case "w" | "write":
			print("write!", args)

		case "s" | "search":
			print("search!", args)

		case "d" | "delete":
			print("delete!", args)

		case "l" | "list":
			print("list!", args)

		case _:
			# throw an error
			print("router!")
		