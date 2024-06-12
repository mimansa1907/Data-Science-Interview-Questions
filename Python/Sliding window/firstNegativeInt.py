from collections import deque
arr = [1,3,4,-1,3,-1,3,-5,-5,2]
k = 3

def getFirstNegative(arr,size):
    res = deque([])
    i= 0
    j =0

    while j < len(arr):
        if arr[j] < 0:
            res.append(arr[j]) 
        
    
        if j-i+1 == size:
            if res:
                print(res.popleft())
            i = i+1
        j = j+1
    return res
        
print(getFirstNegative(arr,k))

