class _Node:
    __slots__='_element','_next'

    def __init__(self,element,next):
        self._element=element #instance variable
        self._next=next
    
class QueueLinked:
    def __init__(self):
        self._front=None #instance variable
        self._rear=None
        self._size = 0

    def __len__(self):
        return self._size 

    def isempty(self):
        return self._size ==0

    def enqueue(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._front = newest
        else :
            self._rear._next = newest
        self._rear = newest
        self._size +=1
    
    def dequeue(self):
        if self.isempty():
            print('Queue is Empty')
            return
        e = self._front._element
        self._front = self._front._next
        self._size -=1
        if self.isempty(): #check if self already one item then all linked is None
            self._rear = None
        return e     

    def first(self):
        if self.isempty():
            print('Queue is Empty')
            return  
        return self._front._element

    def display(self):
        p = self._front
        while p:
            print(p._element,end='<--')
            p = p._next
        print()

Q = QueueLinked()
Q.enqueue(5)
Q.enqueue(3)
Q.display()
print(len(Q))   
Q.enqueue(7)
Q.enqueue(13)
Q.display()
print(len(Q))   
print(Q.dequeue())
Q.display()
print(Q.first())