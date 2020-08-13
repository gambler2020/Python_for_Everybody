class Point:
    def __init__(self, initx, inity):
        self.x=initx
        self.y=inity
    def getx(self):
        return self.x
    def gety(self):
        return self.y
instance1=Point(7,9)
print(instance1.getx())
print(instance1.gety())
