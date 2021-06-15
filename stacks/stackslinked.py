class _Node:
    __slots__='_element','_next'

    def __init__(self,element,next):
        self._element=element #instance variable
        self._next=next

class stackslinked:
    def __init__(self):
        self._top=None #instance variable
        self._size = 0

    def __len__(self):
        return self._size 

    def isempty(self):
        return self._size ==0
    
    def push(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size+=1
    
    def pop(self):
        if self.isempty():
            print('Stack is empty')
            return
        e = self._top._element
        self._top = self._top._next #assign new top to the next point
        self._size -=1
    
    def top(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self._top._element
    
    def display(self):
        p = self._top
        while p:
            print(p._element, end='-->')
            p = p._next
        print()

s = stackslinked()
s.push(1)
s.push(10)
s.push(6)
s.display()
s.pop()
s.display()
print(s.top())
s.display()