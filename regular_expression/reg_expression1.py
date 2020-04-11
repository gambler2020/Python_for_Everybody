import re
fname=input("Enter file name: ")
fhand=open(fname)
for line in fhand:
    line=line.rstrip()
    if re.search("^From", line):
        print(line)
