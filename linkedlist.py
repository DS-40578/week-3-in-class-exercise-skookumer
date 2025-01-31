from node import Node
from book import Book

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def __str__(self):
        return_str = ""
        current = self.head
        while current is not None:
            return_str += str(current)
            current = current.next
        return return_str

    def find_first_index(self, target_value, index = 0):
        current = self.head
        while current is not None:
            if current.data == target_value:
                return index
            current = current.next
            index += 1
    
    def find_last_index(self, target_value, index = 0):
        current = self.head
        indices = []
        while current is not None:
            if current.data == target_value:
                indices.append(index)
            current = current.next
            index += 1
        return max(indices)

    def find(self, target_value):
        current = self.head
        while current is not None:
            if current.data == target_value:
                return current.data
            current = current.next
    
    def to_list(self, list = []):
        current = self.head
        while current is not None:
            list.append(current.data)
            current = current.next
        return list
    
    def count(self):
        return self.head.count()
    
    def calc_price(self):
        return self.head.calculate_price()
    
    # def iterative_filter(self, predicate):
    #     '''
    #     Param: perdicate lambda that takes in a Node
    #     object and returns True/False
    #     '''
    #     current = self.head
    #     new_head = None
    #     while current is not None:
    #         if predicate(current) == True:
    #             new_node = Node(current.data, new_head)
    #             new_head = new_node

    #         current = current.next
    #     return new_head
    
    def iterative_filter(self, predicate):
        '''
        Param: perdicate lambda that takes in a Node
        object and returns True/False
        '''
        current = self.head
        new_ll = LinkedList()
        while current is not None:
            if predicate(current) == True:
                new_ll.add_to_front(current.data)

            current = current.next
        return new_ll
    
    def is_loop(self, list = [], loop = True):
        current = self.head
        while current is not None:
            list.append(current.data)
            if current.next == None:
                loop = False
                return loop
            current = current.next
    
    

#loop
#first make a line
tail_bad = Node("D", None)
m1_bad = Node("A", tail_bad)
m2_bad = Node("B", m1_bad)
head_bad = Node("A", m2_bad)
tail_bad.next = head_bad

    
ll = LinkedList()
ll.add_to_front("C")
ll.add_to_front("A")
ll.add_to_front("B")
ll.add_to_front("A")
ll.add_to_front("C")
ll.add_to_front("A")
ll.add_to_front("B")

print(ll)
print(ll.find("B"))
print("FIRST INDEX", ll.find_first_index("B"))
print("LAST INDEX", ll.find_last_index("B"))
print("TO LIST", ll.to_list())

print(ll.count())


print("--------------------PART 2------------------")

ll = LinkedList()
ll.add_to_front(Book("1"))
ll.add_to_front(Book("nope", True))
ll.add_to_front(Book("linear", False))

print("IS LOOP", ll.is_loop())
print("COUNT", ll.count())

print("CALCULATE PRICE", ll.calc_price())

paperback = lambda node: True if node.data.paperback else False

# new_ll = ll.iterative_filter(paperback)

# print(new_ll)