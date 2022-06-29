def squares(a):
    lst=[]
    for i in range(1,a+1):
        lst.append([i,i**2])
    print(lst)
squares(20)