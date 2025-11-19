from DoubleNode import DoubleNode

class List:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, s):
        self._size = s

    def isEmpty(self):
        return self.head is None

    def first(self):
        return self.head
    
    def last(self):
        return self.tail

    def addFirst(self, data):

        n = DoubleNode(data)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            n.setNext(self.head)
            self.head = n
        self._size += 1

    def addLast(self, data):

        n = DoubleNode(data)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            self.tail.setNext(n)
            self.tail = n
        self._size += 1

    def removeFirst(self):

        if self.isEmpty():
            raise Exception("Lista vacía")
        data = self.head.getData()
        self.head = self.head.getNext()
        self._size -= 1
        if self._size == 0:
            self.tail = None
        return data
    
    def removeLast(self):
        if self._size == 1:
            return self.removeFirst()
        elif self._size > 1:
            anterior = self.head
            while anterior.getNext() is not self.tail:
                anterior = anterior.getNext()
            temp = self.tail
            anterior.setNext(None)
            self.tail = anterior
            self._size -= 1
            return temp.getData()
        else:
            return None


    def eliminarPorAtributo(self, attr, value):

        if self.isEmpty():
            return False
        current = self.head
        prev = None
        while current is not None:
            if getattr(current.getData(), attr) == value:
                if prev is None:
                    self.head = current.getNext()
                else:
                    prev.setNext(current.getNext())
                if current == self.tail:
                    self.tail = prev
                self._size -= 1
                return True
            prev = current
            current = current.getNext()
        return False

    def mostrar(self):
        
        current = self.head
        if current is None:
            print(" (vacía)")
            return
        while current is not None:
            print(current.getData())
            current = current.getNext()