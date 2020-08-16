#write a program to first zip three list and then unzip.
First_name=["Mohammad", "Imran", "Adila"]
Last_name=["Aziz", "Ali", "Afreen"]
City=["Bengaluru", "Birmingham", "Walsall"]
zip1=list(zip(First_name, Last_name, City))
for f_name, l_name, city in zip1:
    print("{} {}, {}".format(f_name, l_name, city))

#procedure for unzipp
First, Last, Cities=zip(*zip1)
print(list(First))
print(list(Last))
print(list(Cities))


