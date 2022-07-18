import sys
# recursion solution
def minimum_path_sum(n,m,mat):
    if n==0 and m ==0:
        return mat[0][0]
    if n<0 or m<0:

        # print(sys.maxsize)
        return sys.maxsize
    up = mat[n][m] + minimum_path_sum(n-1,m,mat)
    left = mat[n][m] + minimum_path_sum(n,m-1,mat)
    return min(up,left)

n,m=2,3
mat = [[5,9,6],[11,5,2]]

print(minimum_path_sum(n-1,m-1,mat))
# memoization solution
def minimum_path_solution_mem(n,m,mat,dp):
    if n==0 and m==0:
        return mat[0][0]
    if n<0 or m<0 :
        return sys.maxsize
    if dp[n][m] != None:
        return dp[n][m]
    up = mat[n][m] + minimum_path_solution_mem(n-1,m,mat,dp)
    left = mat[n][m]+ minimum_path_solution_mem(n,m-1,mat,dp)
    dp[n][m] = min(up,left)
    return dp[n][m]
dp = [[None for _ in range(m)] for _ in range(n)]

print(minimum_path_solution_mem(n-1,m-1,mat,dp))

# tabulation
def minimum_path_solution_tab(n,m,mat,dp):
    for i in range(n):
        for j in range(m):
            if i ==0 and j ==0:
                dp[0][0]= mat[i][j]
            else:
                up,left = sys.maxsize,sys.maxsize
                if i>0:
                    up = mat[i][j] + dp[i-1][j] 
                if j>0:
                    left = mat[i][j]+dp[i][j-1]
                dp[i][j] = min(up,left)
    # print(dp)
    return dp[n-1][m-1]


    

dp = [[None for _ in range(m)] for _ in range(n)]
print(minimum_path_solution_tab(n,m,mat,dp))