def check_numbers(a,b):
        if i%2==0 and j %2==0:
            print("both",i,"and",j, "numbers are even")
        elif i %2==0 and j%2!=0:
            print("Only",i, "is Even but not",j)
        elif i %2!=0 and j%2==0:
            print("Only",j,"is Even but not",i)
        else:
            print("both",i,"and",j,"are odd")

m1 = [50, 60, 10] 
m2 = [10, 20, 13]
for i,j in zip(m1,m2):
    check_numbers(i,j)
