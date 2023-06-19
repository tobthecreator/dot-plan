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
					$ dot-plan - commandline .plan tool [version 1.0]

					Commands: 

					$ plan [options] <command> [command args]
					
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

		case _:
			print("Error: Not a valid command.\nTry '$dot-plan help'")
		