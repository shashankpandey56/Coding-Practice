#tabulation
import sys
# def frog_jump_cost(lst):
#     dp[0]=0
#     for i in range(1,n):
#         left = dp[i-1] + abs(lst[i]-lst[i-1])
#         right = sys.maxsize

#         if i>1:
#             right = dp[i-2]+ abs(lst[i]-lst[i-2])

#         dp[i] = min(left,right)
#     return dp[n-1]

#space optimized solution
def frog_jump_cost(lst):
    prev=0
    prev2=0
    for i in range(1,n):
        left = prev + abs(lst[i]-lst[i-1])
        right = sys.maxsize

        if i>1:
            right = prev2+ abs(lst[i]-lst[i-2])

        curr = min(left,right)
        prev2= prev
        prev = curr
    return curr    


lst = [30,10,60,10,60,50]
n = len(lst)
# dp = [None]*(n)

print(frog_jump_cost(lst))
# print(dp)

