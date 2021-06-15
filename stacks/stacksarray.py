class stacksarray:
    def __init__(self):
        self._data =[]

    def __len__(self):
        return len(self._data)
    
    def isempty(self):
        return self._data == 0
    
    def push(self,e):
        return self._data.append(e)
    
    def pop(self):
        if self.isempty():
            print('Stacks is Empty')
            return
        return self._data.pop()
    
    def top(self):
        if self.isempty():
            print('Stacks is Empty')
            return
        return self._data[-1]

s = stacksarray()
s.push(5)
s.push(3)
print(s._data)
print(len(s))
print(s.pop())
print(s._data)
s.push(12)
print(s._data)
print(s.top())





    
