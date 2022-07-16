# recursive solution
def grid_unique_path(m,n):
    if n==0 and m ==0:
        return 1
    if n<0 or m <0:
        return 0
    up = grid_unique_path(m-1,n)
    left = grid_unique_path(m,n-1)
    return up + left

m,n = 3,3
print(grid_unique_path(m-1,n-1))
#memoization 
def grid_unique_path_mem(dp,i,j):
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0
    if dp[i][j] != None:
        return dp[i][j]
    up = grid_unique_path_mem(dp,i-1,j)
    left = grid_unique_path_mem(dp,i,j-1)
    dp[i][j] = up+left
    return dp[i][j]

dp =[[None for _ in range(m)] for _ in range(n)] 
  

print(grid_unique_path_mem(dp,m-1,n-1))


# Tabulation solution
def grid_unique_path_tab(tab,m,n):
    tab[0][0]=1
    for i in range(m):
        for j in range(n):
            if i ==0 and j==0:
                tab[i][j] = 1
            else:
                up,left = 0,0
                if i >0:
                    up = tab[i-1][j]
                if j >0:
                    left = tab[i][j-1]
                tab[i][j] = up +left
    return tab[m-1][n-1]




tab = [[0 for _ in range(m)] for _ in range(n)]
print(grid_unique_path_tab(tab,m,n))



