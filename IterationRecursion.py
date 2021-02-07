def calculate_itr(n):
    while n > 0: # n+1
        k = n ** 2 #1
        print(k) #1
        n = n - 1 #!

        #O(n+1) = o(n)


def calculate_rec(n): #T(n)
    if n > 0: #1
        k = n ** 2 #1
        print(k) #1
        calculate_rec(n - 1) # not take unit of time  but T(n-1)
        '''
        # 1+1+1+T(n-1) ,n>0
        # 1 ,n=0
        recurrence relation 1. substitution
        T(n) = T(n-n) +n
             =  T(0) +n
             = 1 + n
             =O(1+n) = O(n)             
        '''


calculate_itr(4)
calculate_rec(4) #take unit of time
