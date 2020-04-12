import re
fhand=input("Enter file name: ")
f=open(fhand)
for line in f:
    line=line.rstrip()
    y=re.findall("^From (\S+@\S+)", line)
    print(y)
