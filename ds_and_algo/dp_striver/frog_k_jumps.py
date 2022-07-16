import sys
def frog_jump_cost(i,lst,k):
    if i==0:
        return 0
    min_steps = sys.maxsize
    for j in range(1,k+1):
        if i-j>=0:
            jump = frog_jump_cost(i-j,lst,k) + abs(lst[i]-lst[i-j])
            min_steps = min(jump,min_steps)
    return min_steps
   
   

    


lst = [30,10,60,10,60,50]
n = len(lst)
# dp = [None]*(n+1)
k = int(input())
print(frog_jump_cost(n-1,lst,k))
