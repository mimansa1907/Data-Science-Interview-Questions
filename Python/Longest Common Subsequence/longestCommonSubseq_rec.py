a = 'abcdgh'
b = 'abedfhr'
op = 4 # 'abdh' longest subseq.
# op1 = 2 # 'ab' longest substring

def recursiveLCS(a,b):

    # Base condition
    if len(a) == 0 or len(b) ==0:
        return 0
    
    n = len(a) - 1
    m = len(b) - 1
    # Choice diagram
    # if a[n] == b[m]:
    #     recursiveLCS(a[:n],b[:m])
    # else:
    #    max( recursiveLCS(a,b[:m]) | recursiveLCS(a[:n],b))

    if a[n] == b[m]:
        return 1 + recursiveLCS(a[:n],b[:m])
    else:
        return max( recursiveLCS(a,b[:m]) , recursiveLCS(a[:n],b)) # no one added as no common match found

# print(recursiveLCS(a,b))
m = len(a)
n = len(b)

t = [[-1 for j in range(1001)] for i in range(1001)]

def memoziaLCS(a,b,m,n): # bottom-up

    # t a m+1xn+1 size
    # intialize matrix with -1
    if m==0 or n==0:
        return 0

    if t[m][n] != -1:
        return  t[m][n]
    
    if a[m-1] == b[n-1]:
        t[m][n] = 1+memoziaLCS(a,b,m-1,n-1)
    else:
        t[m][n] = max(memoziaLCS(a,b,m,n-1),memoziaLCS(a,b,m-1,n))
    
    return t[m][n]



def topdownLCS(a,b,m,n):

    t = [[0 for j in range(n+1)] for i in range(m+1)]  ## block represnts subproblem length

    if m==0 or n==0:
        return 0
    
    for i in range(1,m+1):
        for j in range(1,n+1):
    
            if a[i-1] == b[j-1]:
                t[i][j] =  1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    
    return t[-1][-1]

print(topdownLCS(a,b,len(a),len(b)))
    
    

# print(memoziaLCS(a,b,len(a),len(b)))
    







