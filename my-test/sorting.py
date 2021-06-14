def countsort_neg(A):
    minsize = min(A)
    maxsize = max(A) - minsize
    carray = [0]* (maxsize+1)
    for i in A:
        carray[i-minsize] +=1
    j=0
    for i in range(len(carray)):
        while 0<carray[i]:
            A[j]=i+minsize
            j+=1
            carray[i]-=1

def countsort(A):
    n=len(A)
    maxsize = max(A)
    carray = [0]*(maxsize+1)
    for i in range(n):
        carray[A[i]]+=1
    i=0
    j=0
    while i<maxsize+1:
        if carray[i]>0:
            A[j]=i
            j+=1
            carray[i]-=1
        else:
            i+=1

def insertionsort(A):
    n=len(A)
    for i in range (n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position-1]>cvalue:
            A[position]=A[position-1]
            position-=1
        A[position]=cvalue


A = [12,-23,-2,65,1,90,10]
# A = [12,65,1,90,10]
# mergesort(A,0,len(A)-1)
# radixsort(A)
print(A)
insertionsort(A)
print(A)

d 