

#Важливо! Порожня множина створюється тільки через set(), оскільки {} - це порожній словник
empty_set = set()

# list1 = []
# tuple1 = ()
# dict1 = {}

# numbers = {2, 3, 1, 4, 1, 1, 5}
# print(numbers)

# fruits = {"banana", "apple", "cherry"}
# print(fruits)
#
# list1 = [1,2,2,3,4,5,1,2,3,4,7,8,100, 10]
# unique_numbers = set(list1)
# list1 = sorted(list(unique_numbers))
# print(unique_numbers)
# print(list1)
#
# s = {1, 2, 3}
# s.add(4) # Додає елемент
# print(s)

# s = {1,2,3,50,75}
# s.add(100)
# print(s)
# print(hash())
# print(hash(50))
# # print(hash(75))
# # print(hash(3))
# text = 'Python Programming'
#
# # Обчислюємо хеш-значення змінної text
# hash_value = hash(text)
# print(hash_value)
#
# s1 = "banana"
# s2 = "apple"
# s3 = "cherry"
# print(hash(s1))
# print(hash(s2))
# print(hash(s3))

# s = {1, 2, 3}
# s.add(10)
# print(s)
# # s.remove(2)
# # s.discard(8)
# s.pop()
# print(s)
# s.clear()
# print(s)


# A = {1,2,3}
# B = {3,4,5}
# C = A.union(B)
# D = B.union(A)
# E = A | B
# print(C)
# print(D)
# # print(E)
#
# A = {1,2,3}
# B = {2,3,4,5}
# C = A.intersection(B)
# D = B.intersection(A)
# E = A & B
# print(C)
# print(D)
# print(E)
#
# B.intersection_update(A)
# print(f"A = {A}")
# print(f"B = {B}")

# A = {1,2,3}
# B = {3,4,5}
# C = A.difference(B)
# D = B.difference(A)
# E = A - B
# F = B - A
# print(C)
# print(D)
# print(E)
# print(F)
# A.difference_update(B)
# print(f"A = {A}")
# print(f"B = {B}")

# A = {1,2,3}
# B = {3,4,5}
# C = A.symmetric_difference(B)
# D = B.symmetric_difference(A)
# E = A ^ B
# F = B ^ A
# print(C)
# print(D)
# print(E)
# print(F)

# A = {1, 5, 6, 7}
# B = {1, 2, 3, 4}
# print(A.issubset(B))
# print(B.issuperset(A))
# print(A.issuperset(B))
# print(A.isdisjoint(B))

# set1 = set([1,2,3,4])
# print(set1)
# fset = frozenset({1,2,3,4})
# print(fset)


#'r' - read file
#'w' - rewrite file
#'a' - append text to file
#
# str_test = "Hello New Name"
# with open("test.txt", 'w') as file:
#     for i in range(1, 101):
#         file.write('\n' + str_test + str(i))

# file = open("new.txt", 'w')
# file.write("Info")
# file.close()

with open("test.txt", 'r') as file:
    # content = file.read()
    # content_first_line = file.readline(10)
    all_content = file.readlines()
# print(content[0:100])
# print(content_first_line)
# print(all_content[0])
# print(all_content[-1])
print(all_content)
