size =7
window = 3
arr = [2,5,1,8,2,9,2]

import math

def maxSumSubarr(arr, k):
    
    i = 0
    j = 0
    sum = 0
    maxVal = -math.inf
    while j < len(arr):
        sum = sum + arr[j]
        if j-i +1 == k:
            maxVal = max(maxVal,sum)
            sum = sum - arr[i]
            i = i+1
        j = j+1
    return maxVal
print(maxSumSubarr(arr,window))

    
