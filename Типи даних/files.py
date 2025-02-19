# Операції з файлами:
# 'r' - для читання файлу
# 'w' - для переписування файлу
# 'a' - для додавання тексту в кінець файлу

str_test = "Hello New Name"  # Текст, який буде записаний у файл

# Відкриваємо файл для переписування ('w') і записуємо текст 100 разів
with open("test.txt", 'w') as file:  # Відкриваємо або створюємо файл 'test.txt' для запису
    for i in range(1, 101):  # Записуємо рядки з числами від 1 до 100
        file.write('\n' + str_test + str(i))  # Додаємо текст і число на новому рядку

# Відкриваємо новий файл для запису і записуємо "Info"
file = open("new.txt", 'w')  # Відкриваємо або створюємо файл 'new.txt' для запису
file.write("Info")  # Записуємо в файл "Info"
file.close()  # Закриваємо файл

# Читання з файлу 'test.txt'
with open("test.txt", 'r') as file:  # Відкриваємо файл для читання ('r')
    # content = file.read()  # Можна використовувати для читання всього файлу за раз
    # content_first_line = file.readline(10)  # Можна використовувати для читання першої лінії з обмеженням на 10 символів
    all_content = file.readlines()  # Читаємо всі рядки в список

# Можна вивести перші 100 символів з вмісту
# print(content[0:100])  # Потрібно раскоментувати для виведення перших 100 символів
# print(content_first_line)  # Потрібно раскоментувати для виведення першої лінії
# print(all_content[0])  # Вивести перший рядок
# print(all_content[-1])  # Вивести останній рядок
print(all_content)  # Вивести всі рядки, що містяться в списку
