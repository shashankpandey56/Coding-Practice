def combination_sum(i,target,lst):
    if i== len(l)-1:
        if target == 0:
            print(lst)
        return
    if l[i] <= target:   
        lst.append(l[i])
        combination_sum(i,target-l[i],lst)
        print(l[i])
        lst.remove(l[i])
    
    combination_sum(i+1,target,lst)


l = [2,3,6,7]
lst =[]
target =10
combination_sum(0,target,lst)