a = 'adbcbdg'
b = a[::-1]

# b can be a function of string a

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

