'''Ques. 3 : Define a class Order with instance variables as item and price. Define a method show_details()
to display the details of the order. Define a method __gt__() to compare the price of two orders. Create
two objects of the Order class and compare'''

class Order():

    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def show_details(self):
        print(f'Item: {self.item}\n Price: {self.price}')

    def __gt__(self, order2):
        return self.price > order2.price

order1 = Order('Mobile', 100000)
order2 = Order('Laptop', 50000)
print(order1 > order2)
