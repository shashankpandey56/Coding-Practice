# def sum(n,s):
#     if n < 1:
#         print(s)
#         return 
#     sum(n-1,s+n)
   
    


# n = 10

# sum(n,0)
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)
   
    


n = 10

print(sum(n))