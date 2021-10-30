#defining the class

class Rectangle:
    def area(self):
        return (self.length * self.width)

    def __init__(self, length, width):
        self.length = length
        self.width = width

#defining a Vehicle class

class Vehicle:
    max_speed = 0
    mileage = 0

    def __init__(self, sp, age):
        self.max_speed = sp
        self.mileage = age

#defining an empty class

class Vehicle:
    pass

#defining a child class Bus

class Bus(Vehicle):
    pass