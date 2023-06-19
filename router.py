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
					"""
					dot-plan - commandline .plan tool [version 1.0]

					Commands: 

					plan [options] <command> [command args]
					
					l, list  \t[none]         \tList all plan files in the .plan folder
					w, write \t[type] [update]\tWrite an update
					r, read  \t[query]   \tRead a single plan file
					d, delete\t[query]   \tDelete a single plan file

					Update Types:
					?\tQuestion/research topic
					!\tA (hopefully brilliant) idea!
					+\tProgress!
					-\tSetback :/
					*\tTodo
					#\tNote to self

					Query Syntax:
					
					Queries are always in quotes.

					Examples:
					"today"          \tToday's plan file
					"yesterday"      \tYesterday's plan file
					"-3m3w3d"        \tPlan file from 3 months, 3 weeks and 3 days ago. Supports m/w/d
					"3 days ago"     \tPlan file from 3 days ago. Supports m/w/d
					"monday | m"     \tPlan file from the most recent weekday provided, excluding today. Supports all weekdays, and shorthand (m/t/w/r/f/s/u)
					"last monday"    \tSame as above, but from a week ago
					"""
				)
			)

			"""
			$ jq
			jq - commandline JSON processor [version 1.6]

			Usage:    jq [options] <jq filter> [file...]
				jq [options] --args <jq filter> [strings...]
				jq [options] --jsonargs <jq filter> [JSON_TEXTS...]

			jq is a tool for processing JSON inputs, applying the given filter to
			its JSON text inputs and producing the filter's results as JSON on
			standard output.

			The simplest filter is ., which copies jq's input to its output
			unmodified (except for formatting, but note that IEEE754 is used
			for number representation internally, with all that that implies).

			For more advanced filters see the jq(1) manpage ("man jq")
			and/or https://stedolan.github.io/jq

			Example:

				$ echo '{"foo": 0}' | jq .
				{
					"foo": 0
				}

			For a listing of options, use jq --help.
			"""





			# print(
			# 	dedent(
			# 	"""\n
			# 	Valid Commands:
			# 	\tread, r\tread a plan file\targs: <search query>
			# 	\twrite, w\twrite an update to plan file\targs: <note type> <note>
			# 	\tlist, l\tlist all plans in local folder\targs: none
			# 	\thelp, h\tlist all commands\targs: none
			# 	\search, s\tsearch plan files in local folder\targs: TODO finish later

			# 	Valid Note Types:
			# 	\t?\tquestion, research topic
			# 	\t!\tidea
			# 	\t+\tprogress
			# 	\t-\tsetback
			# 	\t*\ttodo
			# 	\t#\tnote to self

			# 	Search Syntax
			# 	\t"today"
			# 	\t"yesterday"
			# 	\t"YYYY-MM-DD"
			# 	\t"MM-DD-YYYY"
			# 	\t"monday", "tuesday", etc, or "m", "t", etc.  Will return most recent plan matching that day of the week, excluding today
			# 	\t"-3m3w3d", supports months, weeks and days
			# 	\t"3 days ago", supports months, weeks and days
			# 	""")
			# )

		case _:
			print("Error: Not a valid command")
		