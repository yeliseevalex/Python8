
# #        0     1      2     3
# list1 = [0, "hello", 2.5, True]
# #        -4    -3     -2    -1
#
# print(list1[1])
# print(list1[-3])

#                         0  1
#               0  1  2    3     4
#       [0  1            2           3  4]
# list2 = [0, 1, [2, 3, 4, [5, 6], 7], 8, 9]
# print(list2[1])
# print(list2[2])
# print(list2[3])
# print(list2[2][1])
# print(list2[2][3][0])

#        0  1     2     3  4  5  6
# list3 = [0, 1, "hello", 3, 4, 5, 6]
# print(list3[1:4])
# print(list3[:4])
# print(list3[4:])
# print(list3[1:6:2])

# list4 = [0, "Hello", 2, 2, True, 4.5, 2]
# print(list4.count(2)) # Повертає кілкість знаходжень переданого елемента
# list4.append(10) # Додає переданий ОДИН елемент в кінець списку
# print(list4)
# list4.extend("Hello") # Додає по-елементно в кінець списка ітерируємий об'єкт
# list4.extend([1,2,3])
# print(list4)
# print(list4.index(2, 3, 10)) # Повертає індекс переданого елеманта
# list4.remove(2)
# print(list4)
# list4.insert(3, False)# Додає елемент False в список на 3 індекс
# print(list4)
# list4.reverse()
# print(list4)
# x = list4.pop(1)
# print(x)
# print(list4)
# list5 = [1,5,6,2,7,4,3]
# list5.sort(reverse=True)
# print(list5)
#
# dict1 = {"name" : "Bob", "age": 25}
# dict2 = {"name" : "Oleg", "age": 25}
# list5.extend([dict1, dict2])
# print(list5)



