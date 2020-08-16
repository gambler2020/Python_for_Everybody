# using class access the zipped values.
city_name=["london", "Birmingham", "Manchester", "Liverpool"]
population=[9000000, 1200000, 511000, 552000]
code=["LN", "BR", "MN", "LP"]
city_details=zip(city_name, population, code)
class City:
    def __init__(self, n, p, c):
        self.name=n
        self.pop=p
        self.Code=c
    def __str__(self):
        return "{}, {}, (Population-{})".format(self.name, self.Code, self.pop)

for city_det in city_details:
    name1, pop1, code1=city_det
    city1=City(name1, pop1, code1)
    print(city1)
