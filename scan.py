import os #Library to handle directory stuff
import sys
import re #library to manage regular expressions
x = re.compile('[a-zA-Z.,+-_=(){};!@#$%^& \[\]]*\.exe'); #This is the regular expression to match any .exe files. Note the escape characters inside RE
fileList = [] #This is a list where i will be storing the filenames.
rootdir = sys.argv[1] #The path inside which .exe files has to be found have to be specified here.
if os.path.lexists(rootdir)==0: #Exception Handling-1 if the path does not exist
	print "The specified path does not exist"
	sys.exit(1)
if os.path.isfile(rootdir): #Exception Handling-2 if the path is not a directory but a file instead
	print "The specified path does not refer to a directory"
	sys.exit(1)
print "The names of the .exe files are\n"
for root, subFolders, files in os.walk(rootdir): #Starting from root go recursively
	for file in files: 
		if re.match(x,file): #Match the regular expression and see if it is a .exe file
			print file
			fileList.append(os.path.join(root,file)) #If yes append the file complete path to the List
print "\n"
print fileList