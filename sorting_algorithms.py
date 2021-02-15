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
'''
# def merge(A,left)
A = [12,23,65,1,90,10]
insertion_sort(A)
print(A)
# print(found)