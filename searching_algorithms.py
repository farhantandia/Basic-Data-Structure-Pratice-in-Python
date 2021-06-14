#compare each value
def linear_search(A, key):
    index = 0
    while (index < len(A)):
        if A[index] ==key:
            return index
        index +=1
    return -1

#divide the array by2 and scan by comparing the bigger or smaller value from the middle index
def binary_iterative(A, key): #must sort the data first
    L=0
    R=len(A)-1
    while (L<=R):
        m = (L+R)//2
        if key == A[m]:
            return m
        elif key < A[m]:
            R = m-1
        elif key > A[m]:
            L = m+1
    return -1

#O(logn)
def binary_recursive(A, key, L,R):
    if L>R: 
        return -1
    else : 
        m = (L+R)//2
        if key == A[m]:
            return m
        elif key < A[m]:
            return binary_recursive(A,key,L,m-1)
        elif key > A[m]:
            return binary_recursive(A,key,m+1,R)

A = [12,23,65,78,90]
# found = binary_recursive(A,78,0,4)
found = binary_iterative(A,78)
print(found)



