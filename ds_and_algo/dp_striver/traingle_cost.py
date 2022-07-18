import sys
# recursion solution
def traingle_min_sum(mat,i,j):
    if i == n-1:
        return mat[i][j]
    d= mat[i][j] + traingle_min_sum(mat,i+1,j)
    dg = mat[i][j] + traingle_min_sum(mat,i+1,j+1)
    
    return min(d,dg)


mat=[[1],[2,3],[3,6,7],[8,9,6,10]]
n = len(mat)

print(traingle_min_sum(mat,0,0))
#memoization
def traingle_min_sum_mem(mat,dp,i,j):
    if i == n-1:
        return mat[i][j]
    if dp[i][j] != None:
        return dp[i][j]
    d= mat[i][j] + traingle_min_sum_mem(mat,dp,i+1,j)
    dg = mat[i][j] + traingle_min_sum_mem(mat,dp,i+1,j+1)
    dp[i][j] = min(d,dg)
    return dp[i][j]
dp =[]
for p in range(n-1):
    lst=[]
    for j in range(p+1):
        lst.append(None)
    dp.append(lst)

print(traingle_min_sum_mem(mat,dp,0,0))

#tabulation
def traingle_min_sum_tab(mat,dp):
    for j in range(n):
        dp[n-1][j] = mat[n-1][j]
    for i in reversed(range(n-1)):
        for j in reversed(range(i+1)):
            d = mat[i][j]+dp[i+1][j]
            dg = mat[i][j]+ dp[i+1][j+1]
            dp[i][j] = min(d,dg)
    return dp[0][0]
   
  




dp =[[None for _ in range(n)] for _ in range(n)]
print(traingle_min_sum_tab(mat,dp))

