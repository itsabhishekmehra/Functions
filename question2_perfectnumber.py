def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        # print("It's a Perfect number.")
        print(num)
    # else:
    #     print(" It's not a perfect number.")
# perfect(497)
for i in range(1,1000):
    perfect(i)