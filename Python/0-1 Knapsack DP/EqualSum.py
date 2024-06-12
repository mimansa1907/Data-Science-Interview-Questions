arr = [1,3,6,2]

# Is equal partition possible? true  or false

def isSubsetPresent(arr,sum):
    if len(arr) == 0 and sum == 0:
        return True
    if len(arr) == 1 and arr[0]<sum:
        return False
    
    n = len(arr)
    val = False
    
    if n>0:
        if arr[n-1] <= sum:
            print(arr)
            print(n)
            val=  (isSubsetPresent(arr[:n-1],sum - arr[n-1])) or (isSubsetPresent(arr[:n-1],sum)) 
        else:
            print(arr)
            print(n)
            val= isSubsetPresent(arr[:n-1],sum) 

    return val

def EqualSum(arr):
    
    ## Sum should be even
    sum =0
    for i in arr:
        sum += i

    if sum % 2 != 0:
        return False

    return isSubsetPresent(arr,sum//2)

print(EqualSum(arr))
