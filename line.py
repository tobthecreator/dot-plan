def CreateLine(t, text):
	match (t):
		case "?" | "!" | "+" | "-" | "*" | "#":
			o = "\n\t{}\t{}"
			return o.format(t, text)
		# case "n":
		# 	return "\n{}\n".format(text)
		case _:
			return "default"
		