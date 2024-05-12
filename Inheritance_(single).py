############## Single Inhitance ##############
class Car:
    # parent class
    @staticmethod
    def start():
        print('Car is started')
    
    # child class
    @staticmethod
    def stop():
        print('Car is stopped')
    
class Tesla(Car):

    def __init__(self, model):
        self.model = model

car1 = Tesla('Model S')

print(car1.model)
print(car1.start())

#### Output: ####

# Model S
# Car is started