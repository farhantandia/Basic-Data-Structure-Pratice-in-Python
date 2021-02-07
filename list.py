person = ["john",'jane','max']
age =[23,24,25]

combine = list(zip(person,age))
print(combine)

x =[('john', 23), ('jane', 24), ('max', 25)]

unzip = list(zip(*x))

print(unzip)
print(unzip[1])

# for i, item in zip(range(len(person)),person):
#     print(i, item)

for i, item in enumerate(person):
    print(i, item)
    if i == 1:
        print('ok')
squares =[]
for i in range (1,101):
    squares.append(i**2)
print(squares)
# sentence = "this is a string"

# print(sentence.split("s"))

# sentence = "this,is,a,string"
# print(sentence.split(","))

