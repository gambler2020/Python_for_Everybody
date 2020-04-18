class partyanimal():
    x=0
    name=""
    def __init__(self, z):
        self.name=z
        print(self.name,"constructed")
    def party(self):
        self.x=self.x+1
        print(self.name, "Party count", self.x)
s=partyanimal("Aziz")
s.party()
j=partyanimal("Modassir")
j.party()
s.party()
