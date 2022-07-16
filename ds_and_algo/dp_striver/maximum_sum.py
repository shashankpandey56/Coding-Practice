# maximum sum of non adjacent element 
#recursive solution
def maximum_sum(i,lst):
    if i == 0:
        return lst[i]
    if i<0:
        return 0
    pick = lst[i] + maximum_sum(i-2,lst)
    not_pick = 0+ maximum_sum(i-1,lst)
    return max(pick,not_pick)

lst = [2,1,4,9]
n = len(lst)

print(maximum_sum(n-1,lst))

# memoization
def maximum_sum_mem(i,lst,dp):
    # print(i)
    if i == 0:
        dp[i] = lst[i]
        return dp[i]
    if i<0:
        return 0
    if dp[i] != None:
        return dp[i]
    # print(dp)
    pick = lst[i] + maximum_sum_mem(i-2,lst,dp)
    not_pick = 0+ maximum_sum_mem(i-1,lst,dp)
    dp[i] = max(pick,not_pick)
    return dp[i]

def maximum_sum_space(n,lst,dp):
    # print(i)
    dp[0]= lst[0]
    for i in range(1,n+1):
        pick = lst[i]
        if i >1:
            pick = pick + dp[i-2]
        n_pick = 0+ dp[i-1]
        dp[i] = max(pick,n_pick) 
    # print(dp)
    return dp[n]
def maximum_sum_space_further(n,lst):
    # print(i)
    prev= lst[0]
    prev2 = 0
    for i in range(1,n):
        pick = lst[i]
        if i >1:
            pick = pick + prev2
        n_pick = 0+ prev
        curr = max(pick,n_pick)

        prev2 = prev
        prev = curr 
 
    return prev

lst = [2,1,4,9]
n = len(lst)
dp = [None]*(n)

# dp with space optimization



print(maximum_sum_mem(n-1,lst,dp))
print('************')
print(maximum_sum_space(n-1,lst,dp))
print('$$$$$$$$$$$$$$$$')
print(maximum_sum_space_further(n,lst))



    
