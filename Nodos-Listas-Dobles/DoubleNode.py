class DoubleNode:
    def __init__(self, data=None, prev=None, next=None):
        self.__data = data
        self.__next = next
        self.__prev = prev

    @property
    def data(self):
        return self.__data
    
    @property
    def next(self):
        return self.__next
    
    @property
    def prev(self):
        return self.__prev
    
    @data.setter
    def data(self, d):
        self.__data = d

    @next.setter
    def next(self, n):
        self.__next = n

    @prev.setter
    def prev(self, p):
        self.__prev = p

