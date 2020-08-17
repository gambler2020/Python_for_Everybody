class ADD:
    def __init__(self, a, b):
        self.x=a
        self.y=b
    def __add__(self, other):
        return ADD(other.x+self.x, other.y+self.y)
    def __str__(self):
        return "{}, {}".format(self.x, self.y)
    def __sub__(self, other):
        return ADD(other.x-self.x, other.y-self.y)
ob1=ADD(1, 2)
ob2=ADD(3, 4)
print(ob1 + ob2)
print(ob1 - ob2)
