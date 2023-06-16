# here we're going to take in all of our CLI commands and parse them out to the right functions

# can make a CMD enum if we care enough

# lots of interesting stuff we can do in here https://learnpython.com/blog/python-match-case-statement/
def Router(cmd, arg):
	match (cmd):
		case _:
			print("router!")
		