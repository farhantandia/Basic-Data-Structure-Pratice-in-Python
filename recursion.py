def fun(n):
    if n>0 :
        k = n**2
        print(k)
        fun(n-1)
fun(4)