from soporte.DoubleNode import DoubleNode
from soporte.Queue import Queue

class BinaryTree:
    def __init__(self, root, size : int):
        self._root = root
        self._size = size
    
    def size(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def isRoot(self, v : DoubleNode):
        return v == self._root
    
    def isInternal(self, v : DoubleNode):
        if v == None:
            return False
        if v.prev == None and v.next == None:
            return False
        else:
            return True
    
    def hasLeft(self, v :  DoubleNode):
        return not(v.prev == None)
    
    def hasRight(self, v : DoubleNode):
        return not(v.next == None)
    
    def left(self, v : DoubleNode):
        return v.prev
    
    def right(self, v : DoubleNode):
        return v.next
    
    def parent(self, v : DoubleNode):
        
        #Revisar Q.first
        
        if self.isRoot(v):
            return None
        else:
            Q = Queue()
            Q.enqueue(self._root)
            temp = self._root
            while not(Q.isEmpty() and self.left(Q.first)) != v and self.right(Q.first != v):
                temp = Q.dequeue
                if self.hasLeft(temp):
                    Q.enqueue(self.left(temp))
                if self.hasRight(temp):
                    Q.enqueue(self.right(temp))
            return Q.first
    
    def depth(self, v : DoubleNode):
        if self.isRoot(v): #caso base
            return 0
        else: #llamado recursivo
            return 1 + self.depth(self.parent(v))
    
    def height(self, v : DoubleNode):
        if not(self.isInternal(v)): #caso base
            return 0
        else: #llamado recursivo
            if self.hasLeft(v) and self.hasRight(v):
                h = max(self.height(self.left(v), self.height(self.right(v))))
            elif not(self.hasLeft(v)):
                h = self.height(self.right(v))
            else:
                h = self.height(self.left(v))
            return 1+h
    
    def addRoot(self, e : object):
        self._root = DoubleNode(e)
        self._size = 1
    
    def insertLeft(self, v : DoubleNode, e : object):
        left = DoubleNode(e)
        v.prev(left)
        self._size += 1
    
    def insertRight(self, v : DoubleNode, e : object):
        right = DoubleNode(e)
        v.next(right)
        self._size += 1
    
    def remove(self, v : DoubleNode):
        p = self.parent(v)
        if self.left(v) or self.hasRight(v): #tiene al menos un hijo - caso 1
            if self.hasLeft(v):
                child = self.left(v)
            else:
                child = self.right(v)
            if self.left(p) == v: #se conecta el hijo de v al padre
                p.prev(child)
            else:
                p.next(child)
            v.prev(None) #se desconecta el nodo v
            v.next(None)
        else: #v no tiene hijos - caso 2
            if self.left(p) == v:
                p.prev(None)
            else:
                p.next(None)
        self._size -= 1