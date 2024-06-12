price = [1,3,4,5,8,12,20] #1,2,3,4,5,6,7
length = 20

## Target maximize profit of cutting

def CutRodMaxProfit(price, length):

    if length == 0 or len(price)==0:  ## if length is zero or array is empty maximum profit we can make is 0
        return 0
    
    n = len(price) # 1,2,3,4,5,6,7
    max_price = 0

    if n>0:
        if n <= length:
            max_price = max(price[n-1] + CutRodMaxProfit(price,length-n),CutRodMaxProfit(price[:n-1],length))
        else:
            max_price = CutRodMaxProfit(price[:n-1],length)

    return max_price

print(CutRodMaxProfit(price,length))