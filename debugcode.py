# #Question1
# def sum():
#     print(12+13)
# sum()

# # Question2
# def welcome():
#     print("Welcome to function")
# welcome()

# # Question3
# def isEven(num):
#     if(num%2==0):
#         print("Even Number")
#     else:
#         print("Odd Number")
# isEven(55)

# Question4
# def say_hello(name):
#     print("Hello ", name)
#     print("How are you?")
# say_hello("Abhishek")

# Example
# def add_numbers(number1, number2):
#     print("I will add two numbers.")
#     print(number1 + number2)
# add_numbers(120, 50)
# num_x = 134
# name = 2
# add_numbers(num_x, name)

# Example
# def say_hello_language(name, language):
#     if language == "hindi":
#         print("Namaste ", name)
#         print("Aap kaise ho?")
#     elif language == "punjabi":
#         print("Sat sri akaal ", name)
#         print("Tuhada ki haal hai?")
#     else:
#         print("Hello ", name)
#         print("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")

# Example
# def say_hello_people(name_x, name_y, name_z, name_a):
#     print("Namaste ", name_x) # In hindi
#     print("Alah hafiz ", name_y) # In urdu
#     print("Bonjour ", name_z) # In french
#     print("Hello ", name_a) # In english 
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")

# Example
# def icecream(*flavours):
#  for i in flavours:
#   print("i love ",i)

# icecream("choclate", "butterscotch","vanilla","strawberry")

# Example
# def attendance(name,status="absent"):
#     print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")

# Question1 Debug 2
# def greet(*names):
#     for name in names:
#         print("Welcome", name)

# greet("Rinki", "Vishal", "Kartik", "Bijender")

# Question2 Debug 2
# def info(name, age = '5'):
#     print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")

# Question3 Debug 2
# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)

# studentDetails("Nilam","loop",'Abhishek')