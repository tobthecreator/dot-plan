import sys
from router import Router

# TODO def LoadCliConfig()
# TODO def LoadProjectConfig() # checks to see if there is a plan folder here


def main():
	def getRouterArgs():
		def extractSysArg(a):
			return a if (a != "") else None

		command = sys.argv[1]
		arg2 = extractSysArg(sys.argv[2])
		arg3 = extractSysArg(sys.argv[3])

		return (command, (arg2, arg3))

	cmd, args = getRouterArgs()
	Router(cmd, args)
	
if __name__ == "__main__":
    main()