line="From aziznitham@gmail.com Sat Jan 5 09:14:16 2020"
words=line.split() #it returns list of words
email=words[1]
piece=email.split("@")
print(piece[1])
