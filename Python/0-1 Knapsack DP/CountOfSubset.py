arr = [2,3,4,6,8,12]
sum = 10

## Recursion
def GetSubsetCount(arr,sum):

    ## Base cases
    if sum==0:
        return 1
    
    if len(arr)==0 and sum>0:
        return 0
    
    n = len(arr) -1 ## start from back
    val =  0

    if n>=0:
        if arr[n] <= sum:
            val += int(GetSubsetCount(arr[:n],sum)) + int(GetSubsetCount(arr[:n],sum-arr[n])) 
        else:
            val += int(GetSubsetCount(arr[:n],sum))
    
    return val

print(GetSubsetCount(arr,sum))