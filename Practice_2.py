'''Ques. 2 : Define a class Employee with instance variables as role, dept, and salary. Define a method
show_details() to display the details of the employee. Define another class Engineer which inherits the
Employee class and has instance variables as name and age. Define a method show_details() to display the
details of the engineer. Create an object of the Engineer class and call the show_details() method.'''

class Employee:

    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print(f'Role: {self.role}\nDepartment: {self.dept}\nSalary: {self.salary}')

class Engineer(Employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__('Engineer', 'IT', 50000)

    def show_details(self):
        print(f'Name: {self.name}\nAge: {self.age}')
        super().show_details()

emp1 = Engineer('Anubhav','21')
emp1.show_details()