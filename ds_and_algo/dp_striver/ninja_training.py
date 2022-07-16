def ninja_training(day,last):
    if day==0:
        maxi =0
        for i in range(0,3):
            if i != last:
                maxi = max(maxi,task[0][i])
        return maxi 
    maxi2 =0
    for i in range(0,3):
        if i != last:
            points = task[day][i] + ninja_training(day-1,i)
            maxi2 = max(points,maxi2)
    return maxi2

# memoization function``
def ninja_training_mem(day,last,dp):
    if day ==0:
        print('reached to day 0')
        print(last,'is last index')
        maxi =0
        for i in range(0,3):
            
            if i != last:
                maxi = max(maxi,task[0][i])
        # dp[day][last]= maxi
        return maxi
    print('&&&&&&&&&&&&7')
    print(dp[day][last])
    if dp[day][last] != None:
        print('dp is not none')
        return dp[day][last]
    maxi2=0
    for i in range(0,3):
        if i != last:
            points = task[day][i] + ninja_training_mem(day-1,i,dp)
            maxi2 = max(points,maxi2)
            print(maxi2)
    # print(dp)
    dp[day][last] = maxi2
    print('dppppppppppppp')
    print(dp[day][last])


task = [[1,2,5], [3 ,1 ,1] ,[3,3,3]]
day = len(task)
dp = [[None]*4]*day
print(ninja_training(day-1,3))
print('***************')
print(dp)
print(ninja_training_mem(day-1,3,dp))
