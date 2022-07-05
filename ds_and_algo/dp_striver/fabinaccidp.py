def fab_dp(n,dp):
    if n<=1:
        return n 
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n]=fab_dp(n-1,dp)+fab_dp(n-2,dp)
    return dp[n]
        



n = 6
dp = [-1]*(n+1)
print(fab_dp(n,dp))