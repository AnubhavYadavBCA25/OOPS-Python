################## Multiple Inheritance ##################

# Parent Class 1
class Car:
    # method 1 of parent class 1
    @staticmethod
    def start():
        print('Car is started')

    # method 2 of parent class
    @staticmethod
    def stop():
        print('Car is stopped')

# Parent Class 2
class Tesla:
    #method 1 of parent class 2
    @staticmethod
    def auto_pilot():
        print('Tesla car is in auto pilot mode')

# Child Class
class Models(Car, Tesla):
    color = 'Color of the car is Red'           # class variable

# Creating object of child class
car1 = Models()
print(car1.color)
print(car1.start())
print(car1.auto_pilot())
print(car1.stop())   

#### Output: ####
# Color of the car is Red
# Car is started
# None
# Tesla car is in auto pilot mode
# None
# Car is stopped