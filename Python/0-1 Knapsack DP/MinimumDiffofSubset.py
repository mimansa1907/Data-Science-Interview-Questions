arr = [1,11,5,5]

def isSubsetPresent(arr,sum):
    if len(arr) == 0 and sum == 0:
        return True
    if len(arr) == 1 and arr[0]<sum:
        return False
    
    n = len(arr)
    val = False
    
    if n>0:
        if arr[n-1] <= sum:
            val=  (isSubsetPresent(arr[:n-1],sum - arr[n-1])) or (isSubsetPresent(arr[:n-1],sum)) 
        else:
            val= isSubsetPresent(arr[:n-1],sum) 

    return val

def MinimumDiffOfSubset(arr):

    ## total sum
    sum = 0
    for i in arr:
        sum += i

    min_diff = sum # sum of all elements - sum of empty array

    ## Let there be two sums, s1 and s2.
    ## s1+s2 = sum
    ## s1,s2 lies in [0,sum]
    ## s2 = sum - s1
    ## Target = min(s1-s2 or s2-s1)
    ## take s1<s2 then we need min(s2-s1)
    ## replace s2 with sum-s1
    ## We need min(sum-2*s1)
    ## s1 will only lower half  values of [0,23]
    ## we need to find what values can S1 take, for given array.
    ## Range of values possible for S1 is half of values between [0,sum/2] mostly
    ## Let's keep s1 between [0,sum/2+1]
    ## let's create arr_s1 with all valid values s1 and simultanoeusly try finding minimum value as well

    for i in range(0,sum//2 +1):
        if isSubsetPresent(arr,i):
            min_diff = min(min_diff,sum-2*i)
            # print(min_diff)
    
    return min_diff

print(MinimumDiffOfSubset(arr))



