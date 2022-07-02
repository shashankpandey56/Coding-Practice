def lever():
    s = input()
    l = s.find('^')
    left,right = 0,0
    
    for i in range(0,l):
        if s[i] != "=":
           left += (l-i)* int(s[i])
       
    for j in range(l+1,len(s)):
        if s[j] != "=":
            right += (j-l)* int(s[j])
       
    if left == right:
        print('balance')
    elif left > right:
        print('left')
    else:
        print('right')
    
    
    
    
    
    
    
    
lever()