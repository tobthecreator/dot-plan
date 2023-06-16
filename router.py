import plan

def Router(cmd, args):
	match (cmd):
		case "r" | "read":
			return plan.ReadPlan2(args)

		case "w" | "write":
			return plan.UpsertPlan(args)

		case "s" | "search":
			return plan.SearchPlans(args)

		case "d" | "delete":
			return plan.DeletePlan2(args)

		case "l" | "list":
			return plan.ListPlans(args)

		case _:
			# TODO throw an error
			print("router!")
		