#################### super() method in inheritance ####################

class Car:

    def __init__(self, type):
        self.type = type

    # method 1 of parent class
    @staticmethod
    def start():
        print('Car is started')

    # method 2 of parent class
    @staticmethod
    def stop():
        print('Car is stopped')

class Tesla(Car):
    def __init__(self,model,type):
        super().__init__(type)
        self.model = model
        super().start()

# Creating object of child class
car1 = Tesla('Model S', 'Electric')
print(car1.type)