''' remove unnecessary space and punctuation '''

punc ='.'
no_punc=''
name = input()                  # Reading input from STDIN
for i in name: # remove punctuation
    if i not in punc:
        no_punc += i
print(" ".join(no_punc.split())) #remove unnecessary space

''' segregate 0 and 1 from string '''
def segregate(arr):
    res = [x for x in arr if x==1]+[x for x in arr if x==0]
    return res
    
name = input()
x = list(map(int, str(name))) #map string to int list
y = segregate(x)
t = [str(int) for int in y] #convert int to list to combine
t = "".join(t)
print(t)

'''output number of vowels from string'''
# Sample code to perform I/O:
def isVowel(ch):
    return ch.lower() in ['a','i','u','e','o']
    
def countVowels(s):
    count=0
    for i in range(len(s)):
        if isVowel(s[i]):
            count+=1
    return count
name = input()  
print(countVowels(name))

'''check how many space in string'''
def check_space(string):
    count=0
    
    for i in range(len(string)):
        if string[i]==" ":
            count+=1
    return count
name = input()                  # Reading input from STDIN
print(check_space(name))         # Writing output to STDOUT


