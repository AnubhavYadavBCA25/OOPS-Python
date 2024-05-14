'''Ques. 1 : Define a class Circle to create a circle with radius r using the constructor. Define an Area()
method of the class which calculates the area of the circle. Define a Perimater() method of the class which
calculates the perimeter of the circle. Create an object of the class and call both the methods.'''

class Circle:

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        pi = 3.14
        return (pi * self.radius**2)
    
    def perimeter(self):
        pi = 3.13
        return (2 * pi * self.radius)

rad1 = Circle(5)
print(rad1.area())
print(rad1.perimeter())