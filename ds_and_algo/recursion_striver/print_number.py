# def func(count):
#     if count ==4:
#         return
#     print(count)
    
#     func(count+1)
# count =0
# func(count)

def func(i,N):
    if i>N:
        return
   
    func(i+1,N)
    print(i)


func(1,5)