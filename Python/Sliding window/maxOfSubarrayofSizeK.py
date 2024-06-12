arr = [1,3,-1,-3,5,3,6,7]
size = 8
window = 3

from collections import deque
def GetMax(arr,window):
    i = 0
    j = 0
    k = window

    deque = []
    max_val=arr[i]

    while j < len(arr):
        max_val = max(max_val,arr[j])


        if j-i + 1 == k:
            deque.append(max_val)

