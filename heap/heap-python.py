import heapq as heap

L1 =[]
heap.heappush(L1,25)
heap.heappush(L1,14)
heap.heappush(L1,2)
heap.heappush(L1,20)
heap.heappush(L1,10)
print(L1)
e=heap.heappop(L1) #meanhip
print(e)
print(L1)
e = heap.heappushpop(L1,1)
print(e)
e = heap.heapreplace(L1,1)
print(e)
print(L1)

L2 = [20,14,2,15,10,21]
heap.heapify(L2)
print(L2)

print(heap.nlargest(3,L2))
print(heap.nsmallest(3,L2))