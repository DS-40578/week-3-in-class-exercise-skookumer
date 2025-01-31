class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
    
    def count(self):
        if self.next is None:
            return 1
        else:
            return 1 + self.next.count()
    
    def calculate_price(self):
        if self.next is None:
            return self.data.price
        return self.data.price + self.next.calculate_price()