def isAnagram(a,b):
    a = a.lower()
    b = b.lower()

    if (len(a)==len(b)):

        if (sorted(a)==sorted(b)):

            print('True')
        else : print('False')
    
    else : print('False')

word1 = 'gigi'
word2 = 'igigi'

isAnagram(word1,word2)
def deleteSpaces(s):
    s_new = s.replace(" ","")
    return s_new
def isAnagram2(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)