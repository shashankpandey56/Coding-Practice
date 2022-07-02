def print_anagram():
    lst = input().split()
    new_dict = {}
    for ele in lst:
        x = ''.join(sorted(ele))
        if x not in new_dict.keys():
            
            new_dict[x] = [ele]
        else:
            new_dict[x].append(ele)
    for ele in new_dict.keys():
        if len(new_dict[ele])>1:
            for e in new_dict[ele]:
                print(e , end =" ")
        print()


print_anagram()