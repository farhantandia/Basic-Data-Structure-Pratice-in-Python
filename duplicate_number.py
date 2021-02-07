def findDuplicate(nums):
    nums.sort()
    for i in range (len(nums)):
        if nums[i]==nums[i-1]:
            return nums[i]
def findDuplicate2(nums):
    seen ={}
    print(seen)
    for num in nums:
        if num in seen:
            return num
        seen[num] = True
# transposed = []
# matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
# print(matrix)
# for i in range(len(matrix[0])):
#     transposed_row=[]
#     for row in matrix:
#         print(row[i])
#         transposed_row.append(row[i])
#         print(transposed_row)
#     transposed.append(transposed_row)
# print(transposed)

# print(findDuplicate2([3,1,3,4,2]))
myList = [ 4,'a', 'b', 'c', 1, 'd', 3]
myint = []
mychar =[]
for i in range(len(myList)):
    if str(myList[i]).isdigit():
        myint.append(myList[i])
    else :
        mychar.append(myList[i])
print(myint)
print(mychar)
myIntList = [x for x in myList if isinstance(x, int)]
myIntList = [x for x in myList if isinstance(x, str)]