# # Question part 1
def add_numbers(num1,num2):
    return num1+num2

# num1=56
# num2=12
# a = add_numbers(num1,num2)
# print(a)


# Question part 2
m1 = [50, 60, 10] 
m2 = [10, 20, 13]
for i,j in zip(m1, m2):
    print(add_numbers(i,j))


# Question part 2 another method
# def add_numbers_list(a,b):
#     for i,j in zip(a,b):
#         print(int(i)+int(j))

# k = input("Enter the list1: ").split(' ')
# m = input("Enterethe list2: ").split(' ')
# add_numbers_list(k,m)