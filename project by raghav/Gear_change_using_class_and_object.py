class person:
    colour = None
    make = None
    speed = None
    gear = None

    def setcolour(self, colour):
        self.colour = colour

    def getcolour(self):
        return self.colour

    def setmake(self, make):
        self.make = make

    def getmake(self):
        return self.make

    def setspeed(self, speed):
        self.speed = speed
        self.setgear()

    def getspeed(self):
        return self.speed
    def setgear(self,):
        if self.speed <= 20:
            self.gear = 1
        elif self.speed <= 40:
            self.gear = 2
        elif self.speed <= 60:
            self.gear = 3
        elif self.speed <= 80:
            self.gear = 4
        elif self.speed <= 100:
            self.gear = 5
        else:
            self.gear = ("It's very high speed...! Enter a speed under 100...! Because Car have max speed is 100. ")

    def getgear(self):
        return self.gear

color = input("Enter the color of the car = ")
make = input("Enter the company name = ")
speed = int(input("Enter the speed of the car = "))


p = person()
p.setmake(make)
p.setcolour(color)
p.setspeed(speed)

print(f"the car is '{p.getmake()}' group of company")
print(f"it's '{p.getcolour()}' colour")
print("the speed of the car = ",p.getspeed())
print(f"the car on {p.getgear()}th gear")

if speed > 80:
    print("the car is above 80 please reduce the speed for safe ride...!")
else:
    print("your very good driver ..! you maintain speed limit nice ..!")

