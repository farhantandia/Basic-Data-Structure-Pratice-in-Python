hexaDeciNum = ['0']*100
# print(hexaDeciNum)
n="2545"
i=0

output_int = 0
if input_str[0]=='-':
    start_idx =1
    is_negative = True
else:
    start_idx = 0
    is_negative = False

    for i in range (start_idx, len(n)):
    place = 


#counter for hex
while(n != 0):

    temp=0

    temp = n%16

    if(temp<10):
        hexaDeciNum[i] = chr(temp+48)
        i +=1
    else :
        hexaDeciNum[i] = chr(temp+55)
        i +=1
    n = int(n/16)
    j=i-1
while (j >=0):
    print((hexaDeciNum[j]), end = "")
    j=j-1
# def dectoHex(n):
