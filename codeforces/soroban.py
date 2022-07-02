def soroban():
    n = int(input())
    lst = []
    if n == 0:
        lst.append(0)
    else:
        while n > 0:
            c = n % 10
            lst.append(c)
            n = n // 10

    # print(lst)

    for ch in lst:
        if ch < 5:
            st = 'O-|'

            l = ch
            rem = 5-l-1
            while l != 0:
                st = st + 'O'
                l = l-1
            if rem > 0:
                st = st + '-'
                while rem != 0:
                    st = st + 'O'
                    rem = rem - 1
            if(len(st) < 8):
                st += "-"

            print(st)
        if ch >= 5:
            st = '-O|'

            l = ch-5
            rem = 5-l-1
            while l != 0:
                st = st + 'O'
                l = l-1
            if rem > 0:
                st = st + '-'
                while rem != 0:
                    st = st + 'O'
                    rem = rem - 1
            if(len(st) < 8):
                st += "-"
            print(st)


soroban()
