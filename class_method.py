################ Class Method ################
'''A class method is bound to the class & receive the class as implicit first argument. 
It is defined using @classmethod decorator.'''

class Car:
    # class  variable
    color = 'Red'

    # class method
    @classmethod        # decorator
    def change_color(cls, color):
        cls.color = color
        print('Color of the car is changed to', cls.color)

# Creating object of the class
car1 = Car()
car1.change_color('Blue')
print(car1.color)
print(Car.color)

# Output:
# Color of the car is changed to Blue
# Blue
# Blue