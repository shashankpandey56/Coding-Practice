def swap_array():
    lst = [1,2,3,4,5,6]
    n = len(lst)
    i=0
    def swap(a,b):
        temp = lst[a]
        lst[a] = lst[b]
        lst[b] = temp
    def func(i):
        if i > n//2:
            return 
        # temp = lst[i]
        # lst[i] = lst[n-i-1]
        # lst[n-i-1]= temp
        # print(lst[i],lst[n])
        swap(i,n-i-1)
        func(i+1)
    func(0)
    print(lst)



swap_array()