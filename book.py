

class Book:
    def __init__(self, title, is_paperback = True):
        self.title = title
        self.paperback = is_paperback
        if self.paperback is True:
            self.price = 9.99
        else:
            self.price = 19.99


    def __str(self):
        return str(self.title)
