arr = [2,3,2,10,5,19] # All    numbers are positive
sum = 40  # given than sum greater than equal to 0 


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

# print(isSubsetPresent(arr,sum))

# def subset_sum(arr, k):
#     def recursion(arr, k, i):
#         # Sum is zero means we have found a subset.
#         if k == 0:
#             return True

#         # At the end of the arr if the sum > 0 then
#         # this subset sum does not equal to sum.
#         if i == len(arr):
#             return False

#         # In case the current arr element is greater than
#         # the sum k only consider excluding the element.
#         if arr[i] > k:
#             return recursion(arr, k, i+1)
#         # To generate all subsets we've to include and exclude
#         # the element at each index.
#         else:
#             return recursion(arr, k-arr[i], i+1) or recursion(arr, k, i+1)

#     return recursion(arr, k, 0)

print(isSubsetPresent(arr,sum))

