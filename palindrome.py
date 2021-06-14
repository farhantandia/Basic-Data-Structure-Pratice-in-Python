
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
cache={}
def fibonacci(A):
    if A in cache:
        return cache[A]
    if A<0:
        return print('icorrect number')
    elif A ==0: return A
    elif A==1 or A==2:return 1
    else:
        value= fibonacci(A-1)+fibonacci(A-2)
    
    cache[A]= value
    return value
c=fibonacci(40)
print(c)
# for i in range(40):
#        print(fibonacci(i))