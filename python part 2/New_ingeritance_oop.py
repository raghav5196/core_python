class shape:
    def __init__(self, color, borderline):
        self.color = color
        self.borderline = borderline

    def getcolor(self):
        return self.color

    def getborderline(self):
        return self.borderline


s = shape("red", 50)

print("color is:",s.getcolor())
print("borderline is:",s.getborderline())
print("_______________________________________________________________________")

class circle(shape):
    def __init__(self, radius,color, borderline):
        super().__init__(color, borderline)
        self.radius = radius

    def getRadius(self):
        return self.radius

    def Area(self):
        return 30 * self.radius * self.radius


c = circle(20,"blue",00)
# print(c.getradius())
print("The area of circle is:",c.Area())
print("The colour of circle is:",c.getcolor())
print("_____________________________________________________________")

class rectangle(shape):
    def __init__(self,lenght,width,color,borderline):
        super().__init__(color,borderline)
        self.lenght = lenght
        self.width = width

    def getLenght(self):
        return self.lenght

    def getWidth(self):
        return self.width
    def Area(self):
        return self.lenght*self.width

r = rectangle(50,40,"black",00)

print("the Lenght of rectangle is:",r.getLenght())
print("width of rectangle is :",r.getWidth())
print("Area of rectangle is :",r.Area())
print("The colour of rectangle:",r.getcolor())