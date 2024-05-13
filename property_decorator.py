################## Property Decorator ##################
'''@property decorator is a built-in decorator in Python which is helpful in defining the properties 
effortlessly without manually calling the inbuilt function property(). Which is used to return the 
property attributes of a class from the stated getter, setter and deleter as parameters.'''

class Student:

    def __init__(self, ml, dl, ai):
        self.ml = ml
        self.dl = dl
        self.ai = ai
    
    @property
    def calPercentage(self):
        return str((self.ml + self.dl + self.ai) / 3) + '%'
    
stu1 = Student(90, 80, 70)
print(stu1.ai)
print(stu1.calPercentage)

# Change AI marks
stu1.ai = 96
print('New Marks of AI subject: ',stu1.ai)
print('New Percentage: ',stu1.calPercentage)

# Output:
# 70
# 80.0%
# New Marks of AI subject:  96
# New Percentage:  88.66666666666667%