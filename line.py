def CreateLine(t, txt):
	match (t):
		case "?" | "!" | "+" | "-" | "*":
			o = "\t{}\t{}"
			return o.format(t, txt)
		case "n":
			return txt
		case _:
			return "default"
		