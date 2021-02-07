class _Node:
    __slots__ = '_element','_left','_right'

    def __init__(self,element,left=None,right=None):
        self._element = element
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root =None

    def maketree(self,e,left,right):
        self._root =_Node(e,left._root,right._root)

    def inorder(self,troot):
        if troot:
            self.inorder(troot.left)
            print(troot._element,end=' ')
            