import sys

#Switch variable on/off for debugging messages.
isDebugging = 0;

#For sending back standard fatal errors. Shuts down program.
def fatal(error_message):
	output = "[!] Fatal error: %s \n"% error_message
	sys.stderr.write(str(output))
	sys.exit(1)

#For sending back warning messages. Will not shut down program.
def warning(warn_message):
	output = "[-] Warning: %s \n" %warn_message
	sys.stdout.write(str(output))

#For sending back debug information.
def debug(bug_message):
	if isDebugging:
		output = "*-Debug---: %s \n"%bug_message
		sys.stdout.write(str(output)) 
		

