############## Single Inhitance ##############

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

# Creating object of child class
car1 = Tesla('Model S')

# Accessing attributes and methods of parent class
print(car1.model)
print(car1.start())

#### Output: ####

# Model S
# Car is started