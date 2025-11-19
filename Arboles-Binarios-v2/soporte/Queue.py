from List import List

class Queue:

    def __init__(self):
        self.data = List()

    def size(self):
        return self.data.size
    
    def isEmpty(self):
        return self.data.isEmpty()

    def enqueue(self, data):

        self.data.addLast(data)

    def dequeue(self):

        return self.data.removeFirst()
    
    def mostrar(self):

        print("Contenido de la cola:")
        self.data.mostrar()