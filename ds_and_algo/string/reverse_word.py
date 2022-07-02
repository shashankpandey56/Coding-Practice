# def reverse_word():
#     s = list(input().split())[::-1]
#     lst = []
#     for ele in s:
#         lst.append(ele)
#     return ' '.join(lst)
    


# print(reverse_word())

words_str0 = "I love Algorithms"
words_str = list(words_str0)

def reverse(words_str, l, r):
  while(l<r):
    tmp = words_str[l]
    words_str[l] = words_str[r]
    words_str[r] = tmp
    l = l+1
    r = r-1

i = 0
j = 0
while(i < len(words_str)):
  try:
    if words_str[j] == ' ':
      reverse(words_str, i, j-1)
      i = j+1
  except IndexError:
    reverse(words_str, i, j-1)
    break
  j = j+1
  
#print(words_str)
words_str.reverse()
print(''.join(words_str))