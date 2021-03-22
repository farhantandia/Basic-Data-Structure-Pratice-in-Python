#comparison : n(n-1)/2 : O(n^2)
#swapping : n-1 : O(n)
#always look the smallest value
#unstable algorithm
def selection_sort(A):
    n=len(A)
    for i in range (n-1):
        position = i
        for j in range(i+1,n): #loop all the array value (left to the right) and comapre with first array value 
            print(j)
            if A[j] < A[position]:
                position=j
        
        temp = A[i]
        A[i]=A[position]
        A[position]=temp

#comparison : n(n-1)/2 : O(n^2)
#swapping : n(n-1)/2 : O(n^2)
#stable
def insertion_sort(A):
    n=len(A)
    for i in range(n):
        cvalue = A[i] #-> holding the element that needs to be inserted at its proper position 
        position = i #compare the element at index of position with cvalue and move the index of the arrat to its left
        while position > 0 and A[position-1]>cvalue: #inserted elements operation and element A(left of c value) is greater than cvalue
            A[position] = A[position-1] #swap the values
            position = position-1 #decremented position 
        A[position] =cvalue #all element to the left of cvalue are smaller and sorted and continue to the next index


'''
Merge Sort
Devide & Conquer
Deviding and merging
O(n log(n))
'''
def mergesort(A,left,right):
    if left < right :
        mid = (left+right)//2
        mergesort(A, left,mid)
        mergesort(A, mid+1,right)
        merge(A,left,mid,right)

def merge(A,left,mid,right):
    i = left
    j = mid+1
    k = left
    B=[0]*(right+1)
    while i <= mid and j <= right:
        if A[i]<A[j]:
            B[k]=A[i]
            i = i +1
        else:
            B[k]=A[j]
            j=j+1
        k=k+1
    
    while i <= mid:
        B[k]=A[i]
        j=j+1
        k=k+1
    
    while j <= right:
        B[k] =A[j]
        j=j+1
        k=k+1

    for x in range(left,right+1):
        A[x]=B[x]

A = [12,23,65,1,90,10]
mergesort(A,0,len(A)-1)
print(A)
# print(found)