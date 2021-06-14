
# def isPalindrome (a):
    
#     return a == a[::-1]

# b = 'nahan'
# a = isPalindrome(b)
# print(a)
# if a:
#     print('yes')
# else: print('no')

# x = 'nahbn'
# w =''

# for i in x :
#     w =i + w

# print(w)
# if w ==x:
#     print('True')
# else: print('False')

def fibonacci(A):
    if A<0:
        return print('icorrect number')
    elif A ==0: return A
    elif A==1 or A==2:return 1
    else:
        return fibonacci(A-1)+fibonacci(A-2)
c=fibonacci(4)
print(c)

def seq_fibonacci(A):
    if A<0:
        return print('icorrect number')
    elif A <=1: return A
    else:
        for i in range(A):