score=input("Enter your score: ")
try:
    s=float(score)
except:
    print("Please enter numeric float number between 0.0 and 1.0")
if s>=0.9:
     print("A")
elif s>=0.8:
     print("B")
elif s>=0.7:
     print("C")
elif s>=0.6:
     print("D")
elif s<0.6:
     print("F")
else:
    print("Enter a suitable float number beyween 0.0 to 1.0")
