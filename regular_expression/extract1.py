# extract numbers from a string

import re
x="My 2 favorite numbers are 9 and 42"
y=re.findall("[0-9]+", x)
print(y)
y.reverse()
print(y)
