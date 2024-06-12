coin = [3,5,7,8,9,10,11]
sum = 500

# def coinChange(arr,sum): ## won't work for very long sequences as the 

#     ## Base cases
#     if sum==0:
#         return 1
    
#     if len(arr)==0 and sum>0:
#         return 0
    
#     n = len(arr) -1 ## start from back
#     val =  0

#     if n>=0:
#         if arr[n] <= sum:
#             val += coinChange(arr,sum-arr[n]) + coinChange(arr[:n],sum)  ## Take nth element or not take it
#         else:
#             val += coinChange(arr[:n],sum)
    
#     return val

# print(coinChange(coin,sum))

# THE DP APPROACH

def change(arr,sum):

    dp = [[0 for j in range(sum+1)] for i in range(len(arr)+1)]
    
    ## make first row as 1
    for i in range(len(arr)+1):
        dp[i][0] =1

    for i in range(1,len(arr)+1):
        for j in range(1,sum+1):
            if arr[i-1] <= j:
                dp[i][j] += dp[i-1][j] + dp[i][j-arr[i-1]]   
            else:
                dp[i][j] +=  dp[i-1][j]    
    
    return dp[-1][-1]

print(change(coin,sum))

        
        
        

