# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum

# sum1 = add_numbers(20, 40)
# print(sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print(sum2)
# print(sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print(number_a)


# def add_numbers_print(number_x, number_y):
#     number_sum = number_x + number_y
#     print (number_sum)
# sum4 = add_numbers_print(4, 5)
# print(sum4)
# print(type(sum4))
# number_b = add_numbers_print(5, 4) / add_numbers_print(2, 1)


# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print("Hello from NavGurukul ;)")
#     return number_sum
#     number_sum = number_x + number_x
#     print("Will i reach here?")
#     return number_sum

# sum6 = add_numbers_more(100, 20)


# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"
#         print("Will I be able to print? :-(")

# mon_menu = menu("monday")
# print(mon_menu)
# tues_menu = menu("tuesday")
# print(tues_menu)
# fri_menu = menu("friday")
# print(fri_menu)

def menu(day):
    if day == "monday":
        food = "Butter Chicken"
    elif day == "tuesday":
        food = "Mutton Chaap"
    else:
        food = "Chole Bhature"
    print("Will I be able to print? :-(")
    return food
    print("But I'm not sure will print? :'(")
print(menu("monday"))