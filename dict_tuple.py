
# my_tuple = (1, 2, 1, 3, 4)
# my_list = [1, 2, 3, 4]
# print(my_tuple)
# print(type(my_tuple))
# print(my_tuple[0])
# print(my_tuple[-1])
# my_list[0] = 5
# print(my_list)
# print(my_tuple.index(1))
# print(my_tuple.count(1))

# my_dict1 = {"name": "Bob", "name1": "Bob"}
# print(my_dict1)
# my_dict2 = {1: "one", 2: "two"}
# print(my_dict2)
my_dict3 = {1: "one", "name": "two", "age": 23, "scores": {"Math": [80.5, 50], "English": 75}}
my_dict4 = {"Hello": 123}
# print(my_dict3[0])
# print(my_dict3["name"])
# print(my_dict3["scores"]["Math"][0])
#
# print(my_dict3.get(1))
# print(my_dict3.get(0))
# print(my_dict3.get("name"))
#
# print(list(my_dict3.items()))
# print(list(my_dict3.keys()))
# print(list(my_dict3.values()))

#1) Якщо ключ існує -> Повертає значення за ключем та не змінює словник
#2) Якщо ключ не існує -> Повертає значення за заумовченням та додає нову пару в словник
# x = my_dict3.setdefault(0, 100)
# print(x)
# print(my_dict3)

# my_dict3.update(my_dict4)
# print(my_dict3)
# # my_dict4.update(my_dict3)
# # print(my_dict4)
#
# x = my_dict3.pop("age")
# print(x)
# print(my_dict3)

# x = my_dict3.pop("age123")
y = my_dict3.popitem()
print(y)
print(my_dict3)
y = my_dict3.popitem()
print(y)
print(my_dict3)
y = my_dict3.popitem()
print(y)
print(my_dict3)
y = my_dict3.popitem()
print(y)
print(my_dict3)
y = my_dict3.popitem()
print(y)
print(my_dict3)
y = my_dict3.popitem()
print(y)
print(my_dict3)
