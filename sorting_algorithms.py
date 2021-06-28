#comparison : n(n-1)/2 : O(n^2)
#swapping : n-1 : O(n)
#always look the smallest value
#unstable algorithm
def selection_sort(A):
    n=len(A)
    for i in range (n-1):
        position = i
        for j in range(i+1,n): #loop all the array value (left to the right) and comapre with first array value 
            # print(j)
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
        i=i+1
        k=k+1
    
    while j <= right:
        B[k] =A[j]
        j=j+1
        k=k+1

    for x in range(left,right+1):
        A[x]=B[x]

def radixsort(A):
    n=len(A)
    maxelement = max(A)
    digits = len(str(maxelement))
    l =[]
    bins = [l]*10
    for i in range(digits):
        for j in range(n):
            e = int((A[j]/pow(10,i))%10)
            if len(bins[e])>0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]
        k=0
        for x in range(10):
            if len(bins[x])>0:
                for y in range(len(bins[x])):
                    A[k]=bins[x].pop(0)
                    k=k+1


def countsort(A):
    n =len(A)
    maxsize = max(A)
    carray = [0]*(maxsize+1)
    for i in range(n):
        carray[A[i]] +=1
    i = 0
    j =0
    while i<maxsize+1:
        if carray[i]>0:
            A[j] =i
            j+=1
            carray[i]-=1
        else:
            i+=1

def countsort_neg(A):
    minsize = min(A)
    maxsize = max(A) - minsize
    carray = [0]*(maxsize+1)
    for i in A:
        carray[i-minsize] += 1
    print(carray)
    # i = 0
    j =0
    for i in range(len(carray)):

        while 0<carray[i]:
            A[j] =i+minsize
            print(A[j])
            j+=1
            carray[i]=carray[i]-1

def quicksort(A,low,high):
    if low < high :
        pi = partition(A,low,high)
        quicksort(A,low,pi-1)
        quicksort(A,pi-1,high)

def partition(A,low,high):
    pivot = A[low]
    i =low
    j=high
    
    while (A[i]<=pivot):
        i+=1
    while (A[j]>pivot):
        j-=1
    if i<j:
        swap(A[i],A[j])

# def swap()
    
'''HeapSort'''
from heap.Heap import Heap

def heapsort(A):
    H= Heap()
    n = len(A)
    for i in range(n):
        H.insert(A[i])
    k=n-1
    for i in range(H._csize):
        A[k] = H.deleteMax()
        k -=1

def bucketsort(A):
    n =len(A)
    maxelement = max(A)
    l = []
    l_buckets = 100000
    buckets =[l]*l_buckets
    for i in range(n):
        j=int(n*A[i]/(maxelement+1))
        if len(buckets[j]) ==0:
            buckets[j] = [A[i]]
        else:
            buckets[j].append(A[i])
    for i in range(l_buckets):
        insertion_sort(buckets[i])
    k=0
    for i in range(l_buckets):
        for j in range(len(buckets[i])):
            A[k]=buckets[i].pop(0)
            k+=1


A = [12,-23,-2,65,1,90.5,90.4]
# mergesort(A,0,len(A)-1)
bucketsort(A)
# radixsort(A)
# print(A)
# A = [63, 250, 835, -947, -651, -128]
print('Original Array:',A)
# selection_sort(A)
print('Sorted Array:',A)
# print(A)

