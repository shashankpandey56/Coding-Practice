def arrange_pallindrome():
    s = input()
    dict1 ={}
    for ele in s:
        if ele not in dict1.keys():
            dict1[ele] = 1
        else:
            dict1[ele] += 1
    odd_count =0
    for ele in dict1.keys():
        if dict1[ele]%2 != 0:
            odd_count += 1
    
    if(odd_count >=2):
        print('can not be arranged as pallindrome')
        return
    else:
        print('can be arranged as pallindrome') 
        return
arrange_pallindrome()