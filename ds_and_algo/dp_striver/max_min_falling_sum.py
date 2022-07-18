import sys
# recursive solution
def max_min_falling_sum(row,col):
    if col <0 or col >m-1:
        return -sys.maxsize - 1
    if row ==0:
        return mat[0][col]

    up = mat[row][col] + max_min_falling_sum(row-1,col)
    ld = mat[row][col] + max_min_falling_sum(row-1,col-1)
    rd = mat[row][col] + max_min_falling_sum(row-1,col+1)
    # print(up,ld,rd)
    return max(up,ld,rd)
mat =[[1,2,10,4],[100,3,2,1],[1,1,20,2],[1,2,2,1]]
n = len(mat)
m = len(mat[0])
ans = -sys.maxsize-1
for j in range(m):
    ans = max(ans,max_min_falling_sum(n-1,j))
print(ans)

print('Memoization')
# memoization
def max_min_falling_mem(row,col,dp):
    if col<0 or col >m-1:
        return -sys.maxsize-1
    if row ==0:
        return mat[0][col]
    if dp[row][col] != None:
        return dp[row][col]
    up = mat[row][col] + max_min_falling_mem(row-1,col,dp)
    ld = mat[row][col] + max_min_falling_mem(row-1,col-1,dp)
    rd = mat[row][col] + max_min_falling_mem(row-1,col+1,dp)
    dp[row][col] = max(up,ld,rd)
    return dp[row][col]
ans =-sys.maxsize-1
dp = [[None for _ in range(m)] for _ in range(n)]
for j in range(m):
    
    ans = max(ans,max_min_falling_mem(n-1,j,dp))
print(ans)


