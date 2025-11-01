class shape:
    def values(self):
        print("This is the base class or parent class")
        self.PI=3.14
        self.r=5.0
        self.l=10
        self.b=10
class circle(shape):
    def area(self):
        area=self.PI*self.r*self.r
        print("area of the cirvle",area)
class rectangle(shape):
    def area(self):
        area=self.l*self.b
        print("areao of rectangle",area)

shape=circle()
shape.values()
shape.area()
shape=rectangle()
shape.values()
shape.area()
