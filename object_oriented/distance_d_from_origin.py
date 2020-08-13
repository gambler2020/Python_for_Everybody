#calculate distance from origin of a circle using class and methods.
class circle:
    def __init__(self, initx, inity):
        self.x=initx
        self.y=inity
    def distance(self):
        d=((self.x**2)+(self.y**2))**0.5
        return d
a=int(input("Enter the value of x coordinate:"))
b=int(input("Enter the value of y coordinate:"))
instance1=circle(a, b)
print(instance1.distance())
