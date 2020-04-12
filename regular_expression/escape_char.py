import re
x="We just received $20.45 for cookies."
y=re.findall("\$[0-9.]+", x)
print(y)
