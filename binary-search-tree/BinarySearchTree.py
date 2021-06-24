class _Node:
    __slots__ = '_element', '_left','_right'

    def __init__(self,element,left=None,right=None):
        self._element = element
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def recinsert(self,troot,e):
        if troot : 
            if e < troot._element:
                troot._left =  self.recinsert(troot._left,e)
            elif e > troot._element:
                troot._right =  self.recinsert(troot._right,e)
        else :
            n = _Node(e)
            troot= n
        return troot
    
    def insert(self,troot,e):
        temp = None
        while troot:
            temp = troot
            if e==troot._element:
                return 
            elif e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right
        n = _Node(e)
        if self._root:
            if e < temp._element:
                temp._left = n
            if e > temp._element:
                temp._right = n
        else:
            self._root = n

    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end=' ')
            self.inorder(troot._right)
    
    def search(self, key):
        troot = self._root
        while troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                troot = troot._left
            elif key > troot._element:
                troot = troot._right
        return False

    def recsearch(self,troot, key):
        if troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                return self.recsearch(troot._left,key)
            elif key > troot._element:
                return self.recsearch(troot._right,key)
        else :
            return False
    
    def delete(self,e):
        p = self._root
        pp = None
        while p and p._element !=e:
            pp = p
            if e < p._element:
                p = p._left
            else :
                p = p._right
        if not p :
            return False

        if p._left and p._right:
            s = p._left
            ps = p
            while s._right:
                ps = s
                s = s._right
            p._element = s._element
            p = s
            pp = ps
        c = None

        if p._left:
            c = p._left
        else:
            c = p._right

        if p == self._root:
            self._root = None
        else:
            if p == pp._left:
                pp._left = c
            else :
                pp._right = c

B = BinarySearchTree()
B._root = B.recinsert(B._root,50)
B.recinsert(B._root,30)
B.recinsert(B._root,80)
B.recinsert(B._root,10)
B.recinsert(B._root,40)
B.recinsert(B._root,60)
B.recinsert(B._root,90)
B.inorder(B._root)
print()
print(B.search(60))
print(B.recsearch(B._root,60))
print()
B.delete(60)
B.inorder(B._root)