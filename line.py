def CreateLine(t, text):
	match (t):
		case "?" | "!" | "+" | "-" | "*" | "#":
			o = "\n{}\t{}"
			return o.format(t, text)
		case _:
			raise print("Error: {} is not a valid update type".format(t))
		