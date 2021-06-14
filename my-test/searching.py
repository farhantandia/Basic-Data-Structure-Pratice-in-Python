def  binary_search(A,key):
    L=0
    R=len(A)-1
    while(L<=R):
        m = (L+R)//2
        if key == A[m]:
            return m
        elif key < A[m]:
            R = m -1
        elif key > A[m]:
            L = m+1
    return -1

def binary_rec(A,key,L,R):
    if L > R:
        return -1
    else :
        m = (L+R)//2
        if key == A[m]:
            return m
        elif key < A[m]:
            return binary_rec(A,key,L,m-1)

        elif key > A[m]:
            return binary_rec(A,key,m+1,R)