#recursive code
mat = [[0,0,0],[0,-1,0],[0,0,0]]
def maze_obstacle(i,j,mat):
    if i>=0 and j>=0 and mat[i][j]==-1:
        return 0
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0
    up = maze_obstacle(i-1,j,mat)
    left = maze_obstacle(i,j-1,mat)
    return up +left



print(maze_obstacle(3-1,3-1,mat))

# memoization
def maze_obstacle_mem(i,j,mat,dp):
    if i>=0 and j>=0 and mat[i][j]==-1:
        dp[i][j]=0
        return 0
    if i ==0 and j ==0:
        dp[i][j]=1
        return 1
    if i<0 or j<0:
        return 0
    if dp[i][j] != None:
        return dp[i][j]
    up = maze_obstacle_mem(i-1,j,mat,dp)
    left = maze_obstacle_mem(i,j-1,mat,dp)
    dp[i][j]=up + left
    return dp[i][j]

dp= [[None for _ in range(3)]for _ in range(3)]
print(maze_obstacle_mem(3-1,3-1,mat,dp)) 

#tabulation
def maze_obstacle_tab(m,n,mat,dp):
    
    for i in range(m):
        for j in range(n):
            if  mat[i][j]==-1:
                dp[i][j]=0
                continue
            if i==0 and j ==0:
                dp[i][j]=1
                continue
            up,left =0,0
            if i>0:
                up = dp[i-1][j]
            if j>0:
                left = dp[i][j-1]
            dp[i][j] = up+left
    return dp[m-1][n-1]

    

dp= [[None for _ in range(3)]for _ in range(3)]
print(maze_obstacle_tab(3,3,mat,dp))

