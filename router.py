import plan
from textwrap import dedent

def Router(cmd, args):
	match (cmd):
		case "r" | "read":
			return plan.ReadPlan(args)

		case "w" | "write":
			return plan.UpsertPlan(args)

		case "s" | "search":
			return plan.SearchPlans(args)

		case "d" | "delete":
			return plan.DeletePlan(args)

		case "l" | "list":
			return plan.ListPlans(args)

		# TODO - this is very below my bar. find a pretty print table version 
		case "h" | "help":
			print(
				dedent(
				"""\n
				Valid Commands:
				\tread, r\tread a plan file\targs: <search query>
				\twrite, w\twrite an update to plan file\targs: <note type> <note>
				\tlist, l\tlist all plans in local folder\targs: none
				\thelp, h\tlist all commands\targs: none
				\search, s\tsearch plan files in local folder\targs: TODO finish later

				Valid Note Types:
				\t?\tquestion, research topic
				\t!\tidea
				\t+\tprogress
				\t-\tsetback
				\t*\ttodo
				\t#\tnote to self

				Search Syntax
				\t"today"
				\t"yesterday"
				\t"YYYY-MM-DD"
				\t"MM-DD-YYYY"
				\t"monday", "tuesday", etc, or "m", "t", etc.  Will return most recent plan matching that day of the week, excluding today
				\t"-3m3w3d", supports months, weeks and days
				\t"3 days ago", supports months, weeks and days
				""")
			)

		case _:
			print("Error: Not a valid command")
		