import sys
from router import Router

# TODO def LoadCliConfig()
# TODO def LoadProjectConfig() # checks to see if there is a plan folder here


def main():
	def getRouterArgs():
		def extractSysArg(a):
			return a if (a != "") else None

		print('[0]', sys.argv[0])
		command = sys.argv[1]
		args = sys.argv[2:]

		return (command, args)

	cmd, args = getRouterArgs()
	Router(cmd, args)
	
if __name__ == "__main__":
    main()