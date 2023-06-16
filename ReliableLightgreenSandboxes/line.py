def CreateLine(t, txt):
	match t:
		case "?" | "!" | "+" | "-" | "*":
			o = "\t{}\t{}"
			return o.format(t, txt)
		case "n" | _:
			return txt
		