def run_length_encoding():
    s = input()
    i =0 
    new_s = ""
    n = len(s)
    while(i<n):
        count = 1
        while(i+1<n and s[i]==s[i+1]):
            count = count+1
            i =i +1
        new_s += s[i] + str(count)
        i +=1
    print(new_s)
        

        

    
run_length_encoding()