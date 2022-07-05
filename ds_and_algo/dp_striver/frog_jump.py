import sys
def frog_jump_cost(i,dp,lst):
    if i==0:
        return 0
    if dp[i] != None:
        return dp[i]
    left = frog_jump_cost(i-1,dp,lst) + abs(lst[i]-lst[i-1])
    right = sys.maxsize

    if i>1:
        right = frog_jump_cost(i-2,dp,lst) + abs(lst[i]-lst[i-2])

    dp[i] = min(left,right)
    return dp[i]
    


lst = [30,10,60,10,60,50]
n = len(lst)
dp = [None]*(n+1)

print(frog_jump_cost(n-1,dp,lst))
