def smallest_window():
    pat = input()
    s = input()
    hp = {}
    hs = {}
    for ele in pat:
        if ele not in hp.keys():
            hp[ele] = 1
        else:
            hp[ele]+= 1
    for ele in s :
        if ele not in hs.keys():
            hs[ele] =1
        else:
            hs[ele] += 1
    min_len = 10000
    start = 0 
    end =0 
    