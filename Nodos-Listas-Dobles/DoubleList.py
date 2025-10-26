from DoubleNode import DoubleNode

#Clarificaciones al llamar getters o setters:
#first = head
#last = tail

#Recordar:
#head y tail pueden ser objetos de la clase DoubleNode
#addFirst y addLast ya incrementan el tamaño de por si

class DoubleList:
    def __init__(self, head=None, tail=None, size = 0):
        self.__head = head
        self.__tail = tail
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @property
    def first(self):
        return self.__head
    
    @property
    def last(self):
        return self.__tail
    
    @size.setter
    def size(self, s):
        self.__size = s

    @first.setter
    def first(self, f):
        self.__head = f

    @last.setter
    def last(self, l):
        self.__tail = l
    
    def isEmpty(self):
        return self.size == 0
    
    def addFirst(self, e):
        n = DoubleNode(e) #Nuevo nodo con el dato e
        if self.isEmpty(): #Si la lista esta vacia, el nuevo nodo es la cabecera y la cola
            self.first = n
            self.last = n
        else: #conexion con el nuevo nodo
            n.next = self.first
            self.first.prev = n 
            self.first = n #actualizamos la cabecera
        self.size += 1

    def addLast(self, e):
        n = DoubleNode(e)
        if self.isEmpty():
            self.first = n
            self.last = n
        else:
            self.last.next = n
            n.prev = self.last
            self.last = n #actualizamos la cola
        self.size += 1

    def removeFirst(self):
        if not self.isEmpty(): #de lo contrario no habria nada para eliminar lol
            temp_dato = self.first.data
            if self.size == 1: #caso de que solo haya un nodo
                self.first = None
                self.last = None
            else: #Un caso cualquiera de una lista con varios nodos
                temp = self.first.next #variable temporal que almacena la nueva cabecera
                self.first.next = None
                temp.prev = None
                self.first = temp
            self.size -= 1
            return temp_dato
        return None
        
    def removeLast(self):
        if not self.isEmpty():
            temp_dato = self.last.data
            if self.size == 1:
                self.first = None
                self.last = None
            else:
                temp = self.last.prev
                self.last.prev = None
                temp.next = None
                self.last = temp
            self.size -= 1
            return temp_dato
        return None
        
    def remove(self, n):
        if n==self.first:
            return self.removeFirst()
        elif n==self.last:
            return self.removeLast()
        else:
            temp_dato = n.data
            temp_prev = n.prev
            temp_next = n.next

            temp_prev.next = temp_next
            temp_next.prev = temp_prev

            n.next = None
            n.prev = None

            self.size -= 1
            
            return temp_dato
        
    def addAfter(self, n, e):

        #n -> nodo al que queremos agregar uno nuevo despues de este
        #e -> nodo que queremos agregar despues de n

        if n==self.last:
            self.addLast(e)
        else:
            m = DoubleNode(e)
            temp = n.next

            n.next = m
            m.prev = n
            m.next = temp
            temp.prev = m
            self.size += 1

    def addBefore(self, n, e):
        if n == self.first:
            self.addFirst(e)
        else:
            m = DoubleNode(e)
            temp = n.prev
            temp.next = m
            m.prev = temp
            m.next = n
            n.prev = m
            self.size += 1