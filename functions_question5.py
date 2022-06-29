def calculator(number_x,number_y,operation):
    if operation=="add":
        return number_x+number_y
    elif operation=="subtract":
        return number_x-number_y
    elif operation=="multiply":
        return number_x*number_y
    elif operation=="divide":
        return number_x/number_y

def list_change(a,b):
    m=[]
    for i,j in zip(a,b):
        m.append(calculator(i,j,"multiply"))
    return m
multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])
print(multiple_list)



# print(calculator(20, 25, "add"))
# print(calculator(40, 3, "subtract"))
# print(calculator(10, 4, "multiply"))
# print(calculator(40, 4, "divide"))
# number_1= calculator(24, 20, "add")
# number_2= calculator(24, 20, "multiply")
# number_3= calculator(24, 20, "divide")
# number_4= calculator(24, 20, "subtract")

# print("num1",number_1)
# print("num2",number_2)
# print("num3",number_3)
# print("num4",number_4)


# a =int(input("Enter first numbers: "))
# b= int(input("Enter second number: "))
# add_result= calculator(a,b, "add")
# subtract_result= calculator(a,b, "subtract")
# multiply_result= calculator(a,b, "multiply")
# divide_result= calculator(a,b, "divide")
# print(add_result)
# print(subtract_result)
# print(multiply_result)
# print(divide_result)