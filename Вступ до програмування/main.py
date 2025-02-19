# number1 = 5
# number2 = 5
# print(number1, number2)
# str1 = "Hello"
# str2 = "5"
# print(number1 + number2)
# print(number1 + str2) #Error


# name = input("Enter your name: ")
# print(name)
# print(type(name))

# number3 = int(input('Enter number: '))
# print(number3 + 5)
# print(type(number3))

# print("Hello world")

# num_10 = 16
# num_2 = bin(num_10)
# num_8 = oct(num_10)
# num_16 = hex(num_10)
# print(num_10) # 0 1 2 3 4 5 6 7 8 9
# #15
# # 8
# #23
# print(num_2) # 0 1
# # 000 -> 0
# # 001 -> 1
# # 010 -> 2
# # 011 -> 3
# # 100 -> 4
# # 101 -> 5
# # 110 -> 6
# # 111 -> 7
# print(num_8) # 0 1 2 3 4 5 6 7
# print(num_16) # 0 1 2 3 4 5 6 7 8 9 a b c d e f

# print(2.0+2)
# print(2-2.0)
# print(2*2.0)
# print(2/2)
# print(type(2/2))

# number4 = 2.999999
# number5 = 2.0
# print(3.5468445616516510*5.84601651)
# print(int(number4))
# print(int(number5))

# number4 = 2
# number5 = 2
# print(float(number4))
# print(float(number5))

# bool_True = True
# bool_False = False
# print(bool_True)
# print(bool_False)

# print(5 < 5)
# print(5 > 5)
# print(5 <= 5)
# print(5 >= 5)
# print(5 == 5)
# print(5 != 5)

# number6 = 5
# print(-number6)

# print(2**5)

# print(5 // 2)
# print(5 % 2)
# 5 | 2
#-
# 4 | 2
#______
# 1
#
# s_per_m = 60
# m_per_h = 60
# h_per_day = 24
# result_task3 = s_per_m * m_per_h * h_per_day
# print("Result task 3 -", result_task3, "seconds")
# days_per_year1 = 365
# days_per_year2 = 366
# result_task4_1 = days_per_year1 * result_task3
# result_task4_2 = days_per_year2 * result_task3
# print("Result task 4_1 -", result_task4_1, "seconds")
# print("Result task 4_2 -", result_task4_2, "seconds")
# name_new_planet = input("Name new planet: ")
# days_in_new_planet = int(input("Days in new planet: "))
# result_task5 = days_in_new_planet * result_task3
# print("In new planet", name_new_planet, result_task5, "seconds in one year")

monthly_age = int(input("Enter monthly age: "))
year_age = monthly_age / 12
print(year_age > 18, "Year age", year_age)

monthly_age = int(input("Enter monthly age: "))
year_age = monthly_age // 12
print(year_age >= 18, "Year age", year_age)
