def multiple(a):
    lst=[]
    for i in range(1,a+1):
        if i%3==0 or i%5==0:
            lst.append(i)
    print(lst)
    print(sum(lst))
# multiple(10)
from pratik_function import prime

print(prime(3))