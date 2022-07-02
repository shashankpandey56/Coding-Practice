def subseq(i,lst):
    if i >= len(l):
        print(lst)
        return 
    lst.append(l[i])
    subseq(i+1,lst)
    lst.remove(l[i])
    subseq(i+1,lst)

l = [3,1,2]
lst =[]
subseq(0,lst)