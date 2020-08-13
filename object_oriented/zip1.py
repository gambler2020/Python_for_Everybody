# zip() function is used to map the similar index of multiple container.
name=["Aziz", "Jav", "Mod", "Tam"]
roll_no=[4,3,7,9]
marks=[50,60,40,30]
mapped=zip(name, roll_no, marks)
mapped=set(mapped)
print(mapped)
