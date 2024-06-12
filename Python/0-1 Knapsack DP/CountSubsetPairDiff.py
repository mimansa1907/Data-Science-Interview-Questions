arr = [0,2,3,5,6,9,12]
diff = 3

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

def CountSubsetPairDiff(arr,diff):

    ## let s1 and s2 be sum of two subsets
    ## we know s1+s2 = sum(arr)
    ## given s1-s2 = diff
    ## therefore 2s1 = sum(arr) - diff
    ## s1 = (sum(arr) - diff)/2

    sum_arr = 0

    for i in arr:
        sum_arr += i
    print(sum_arr)

    s1 = int((sum_arr + diff)/2)
    print(s1)

    return GetSubsetCount(arr,s1)

print(CountSubsetPairDiff(arr,diff))


## EXTENSION
# Target Sum
# arr = [1,1,2,3]
# sum = 1
# add + or - in front of each number
# consider +1 -1 -2 +3
# same as [1,3] - [1,2] = 1
# same as count subset with given difference