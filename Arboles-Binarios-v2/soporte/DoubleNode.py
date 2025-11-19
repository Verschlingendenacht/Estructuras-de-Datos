class DoubleNode:
    def __init__(self, value=None, left=None, right=None ):
        self.__value = value
        self.__left = left
        self.__right = right

    @property
    def data(self):
        return self.__value
    
    @property
    def next(self):
        return self.__right
    
    @property
    def prev(self):
        return self.__left
    
    @data.setter
    def data(self, d):
        self.__value = d

    @next.setter
    def next(self, n):
        self.__right = n

    @prev.setter
    def prev(self, p):
        self.__left = p

    def __str__(self):
        return str(self.value)