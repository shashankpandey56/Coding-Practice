# def first_non_repeating_char():
#     s = input()
#     dict1 ={}
#     for ele in s:
#         if ele not in dict1.keys():
#             dict1[ele] = 1 
#         else:
#             dict1[ele] += 1
#     for ele in s :
#         if dict1[ele] ==1:
#             print(ele)
#             return 
# first_non_repeating_char()

def first_non_repeating_char_stream():
    cnt_dict={}
    idx_dict = {}
    idx = 0
    while True:
        x = input('Enter a character')
        if x not in cnt_dict.keys():
            cnt_dict[x] = 1
            idx_dict[x] = idx
            idx += 1
        else:
            cnt_dict[x] += 1
            idx = idx +1 
        unique =[]
        for ele in cnt_dict.keys():
            if cnt_dict[ele]==1:
                unique.append(ele)
        min_idx = 1000
        val = None
        for ele in unique:
            if min_idx > idx_dict[ele]:
                min_idx = idx_dict[ele]
                val = ele
        print(val)
        

print(first_non_repeating_char_stream())