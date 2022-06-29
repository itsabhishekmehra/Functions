# max function
# numbers = [3, 5, 7, 34, 2, 89, 2, 5]
# print(max(numbers))


# sum function
# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))


# sort function
# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# unorder_list.sort()
# print(unorder_list)


# reverse function
# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# reverse_list.reverse()
# print(reverse_list)


# min function
# list = [8, 6, 4, 8, 4, 50, 2, 7]
# print(min(list))

# def sum_karke_de(num):
#     if num%2==0:
#         print("Even:",num)
#         return 
#     print("ODD", num)

# for i in range(10):
#     sum_karke_de(i)

# l = [8, 6, 4, 8, 4, 50, 2, 7]
# def check_num(num_list, num):
#     return num in num_list
# response = check_num(l, 33) # True
# print(response) #False
# r = l.pop(-1) #4
# print(check_num(l,r)) #False

def tellwovel(pucho):
    b = 'aeiouwy'
    count=0
    for i in pucho.lower():
        if i in b:
            # print(i)
            count+=1
    return count
# print(tellwovel('pratiiiiik'))
    
def myfun(args):
    print(args)
myfun(2,3,"Pratik")