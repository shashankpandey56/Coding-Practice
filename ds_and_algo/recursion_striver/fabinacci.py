def fabinacci(n):
    if n <= 1:
        return n
    return fabinacci(n-1) +fabinacci(n-2)


print(fabinacci(6))