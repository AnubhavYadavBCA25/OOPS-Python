################### Multi-level Inheritance ####################

# Parent Class
class Car:
    # method 1 of parent class
    @staticmethod
    def start():
        print('Car is started')

    # method 2 of parent class
    @staticmethod
    def stop():
        print('Car is stopped')

# Child Class
class Tesla(Car):
    def __init__(self, model):
        self.model = model

# Grandchild Class (Child class of 'Tesla' class)
class Models(Tesla):
    def __init__(self, color):
        self.color = color

# Creating object of grandchild class
car1 = Models('Red')
print(car1.color)
car1.model = 'Model S'
print(car1.model)
print(car1.start())

#### Output: ####

# Red
# Model S
# Car is started