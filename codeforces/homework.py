def child_and_homework():
    a = input().split('.')[-1]
    b = input().split('.')[-1]
    c= input().split('.')[-1]
    d = input().split('.')[-1]
    
    lst = []
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.append(d)
    indices =[]
    
    for i in range(len(lst)-1):
        num = 0
        for j in range(len(lst)-1):
            if lst[j] > lst[i]*2:
                num = num +1
                print('adding nums',num)
            if lst[j] < lst[i]*2:
                num = num -1
                print('subtract num',num)
        if num == 3 or num == -3:
            print('index append num',num)
            indices.append(i)
    if len(indices)==1:
        if indices[0] == 0:
            print('A')
        elif indices[0] == 1:
            print('B')
        elif indices[0] == 2:
            print('C')
        else:
            print('D')
    else:
        print('C')

    
    
    
    
child_and_homework()