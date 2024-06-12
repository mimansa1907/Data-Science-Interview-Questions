a = 'abcde'
b = 'abfce'

o= 2


def LongestCommonSubstring(a,b,m,n):

    # Base case
    if m == 0 or n==0:
        return 0
    
    t = [[0 for j in range(n+1)] for i in range(m+1)]  ## block represnts subproblem length
    
    max_len = 0
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1] == b[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
                max_len = max(t[i][j],max_len)
            else:
                t[i][j] = 0
    
    return max_len

print(LongestCommonSubstring(a,b,len(a),len(b)))
