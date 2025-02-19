
# import datetime
from datetime import datetime, timedelta

# print(datetime.now())
# print(datetime(2025, 2, 7, 15, 13, 30))
# print((datetime.now() - datetime(2000, 2, 7, 15, 13, 30)))
#
# print(datetime(2025, 2, 7, 15, 13, 30).year)
# print(datetime(2025, 2, 7, 15, 13, 30).month)
# print(datetime(2025, 2, 7, 15, 13, 30).day)
# print(datetime(2025, 2, 7, 15, 13, 30).second)
# print(type(datetime.now().minute))

# print((datetime.now() - datetime(2000, 2, 7, 15, 13, 30)).seconds)
# print((datetime.now() - datetime(2000, 2, 7, 15, 13, 30)).days)
# print((datetime.now() - datetime(2000, 2, 7, 15, 13, 30)).microseconds)
# print((datetime.now() - datetime(2000, 2, 7, 15, 13, 30)).total_seconds())

# print(datetime.now().strftime("%d.%m.%Y"))
# print(datetime.now().strftime("%d.%m.%y"))
# print(datetime.now().strftime("%d%Y%m"))
# print(datetime.now().strftime("%a")) # Абревіатура дня тижня
# print(datetime.now().strftime("%A")) # Повна назва дня тижня
# print(datetime.now().strftime("%w")) # День тижня як число (0=Неділя, 6=Субота)
# print(datetime.now().strftime("%d")) # День місяця (01 - 31)
# print(datetime.now().strftime("%b")) # Абревіатура місяця
# print(datetime.now().strftime("%B")) # Повна назва місяця
# print(datetime.now().strftime("%m")) # Місяць як число
# print(datetime.now().strftime("%y")) # Рік як двозначне число
# print(datetime.now().strftime("%Y")) # Рік як чотиризначне число
# print(datetime.now().strftime("%H")) # Година у 24-годинному форматі
# print(datetime.now().strftime("%I")) # Година у 12-годинному форматі
# print(datetime.now().strftime("%p")) # AM або PM
# print(datetime.now().strftime("%M")) # Хвилини
# print(datetime.now().strftime("%S")) # Секунди
# print(datetime.now().strftime("%f")) # Мікросекунди
# print(datetime.now().strftime("%j")) # День року (001-366)
# print(datetime.now().strftime("%U")) # Номер тижня (00 - 53), неділя є першим днем тижня
# print(datetime.now().strftime("%W")) # Номер тижня (00 - 53), понеділок є першим днем тижня
# print(datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f %I:%M:%S.%f%p %A %B"))

# date_str = "02/07/2025"
# date_datetime = datetime.strptime(date_str, "%d/%m/%Y")
# print(date_datetime.day)
# print(date_datetime)

# import sys
# sys.set_int_max_str_digits(100000)
# t1 = datetime.now()
# print(2**100000)
# t2 = datetime.now()
# print((t2 - t1).microseconds)# 36827

# t1 = datetime.now()
# result = 2**100000
# result2 = result*2000000
# print(result*2000000)
# t2 = datetime.now()
# print((t2 - t1).microseconds)

# def greet(name, age):
#     print(f"Hello {name} {age}")
    # return f"Hello {name} {age}"

# print(greet("Bob", 45))
# print(greet("Alice", 35))

# def summa(a, b):
#     # print(a + b)
#     return a + b

# result = summa(4,5)
# print(result + 5)
# result = summa(4,5)
# print(result + 5)

# for i in range(1,11):
#     result = summa(i, i+1)
#     print(f"Summa {i} + {i+1} = {result}")


# def summa(a=2, b=0):
#     return a + b
#
# result = summa(b=5)
# print(result)

# def summa(*nums):
#     result = 0
#     for i in nums:
#         result += i
#     return result
#
# result = summa(1,2)
# result2 = summa(2,3,4,5)
# print(result)

# def greet(**info):
#     # print(info.items())
#     # print(info.values())
#     # print(info.keys())
#     for key, value in info.items():
#         print(f'Key {key} - value {value}')
#
# greet(name="Bob",age=25)

def summa(num1: int, num2: int) -> int:
    """Повертає суму num1 + num2"""
    return num1 + num2


print(summa(5, 5))

