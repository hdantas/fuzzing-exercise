import readfile

filename = "output.txt"
while(1):
	print "Enter a file name:",
	tmp = raw_input()
	if tmp != "":
		filename = tmp
	newfile = readfile.ReadFile();
	newfile.readfile(filename)