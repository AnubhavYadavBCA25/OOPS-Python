############## Polymorphism & Operator Overloading ##############

'''Polymorphism: The ability to use a common interface for multiple forms (data types).'''

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_num(self):
        print(f'{self.real}i + {self.img}j')

    def __add__(self, num2):            # Addition dunder method
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)
    
    def __sub__(self, num2):            # Substruction dunder method
        new_real = self.real - num2.real
        new_img = self.img - num2.img
        return Complex(new_real, new_img)
    
num1 = Complex(3,4)
num2 = Complex(5,6)

num3 = num1 + num2
num4 = num1 - num2

num3.show_num()
num4.show_num()

# Output:
# 8i + 10j
# -2i + -2j