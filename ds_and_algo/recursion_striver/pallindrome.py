
def pallindrome(i):
    if i>= n//2:
        return True
    if s[i] != s[n-i-1]:
        return False
    return pallindrome(i+1)




s= 'kayak'
i=0
n= len(s)
print(pallindrome(i))