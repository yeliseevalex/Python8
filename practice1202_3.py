# ## Завдання 3. Підземелля скарбів
# 
# 1. Структура підземелля:  
#    - Використовуйте словник (dict) для опису кімнат підземелля.  
#      - Ключ – назва кімнати (наприклад, `"вхід"`, `"кімната 1"`, `"кімната 2"`, `"кімната 3"`, `"скарбниця"`).  
#      - Значення – інший словник, де ключі – можливі напрямки (наприклад, `"вперед"`, `"назад"`, `"праворуч"`, `"ліворуч"`),
#           а значення – назви суміжних кімнат.
#    - Для кімнати `"скарбниця"` додайте можливість виходу (наприклад, напрямок `"назад": "кімната 3"`).
# 
# 2. Вміст кімнат:  
#    - Зберігайте вміст кожної кімнати у окремому словнику (`room_contents`).  
#    - Можливі варіанти вмісту:
#      - `"скарб"` – дає +10 очок.
#      - `"великий скарб"` – дає +50 очок (зазвичай знаходиться в кімнаті `"скарбниця"`).
#      - `"монстр"` – завдає випадкову шкоду від 10 до 30 одиниць.
#      - `"здоров'я"` – дає бонус до здоров’я (випадкове число від 7 до 15).
#      - `"порожньо"` – кімната порожня.
#    - Початкове вміст кімнат (крім `"вхід"` та `"скарбниця"`) генерується випадковим чином з використанням `random.choices`
#       із заданими вагами (наприклад, збільшено шанс появи монстра).
# 
# 3. Статистика гравця:  
#    - Зберігайте у словнику параметри гравця:  
#      - `здоров'я` (початкове значення 100).  
#      - `скарби` (початкове значення 0).  
#      - `поточна_кімната` (починається з `"вхід"`).
# 
# 4. Рух та ігровий процес:  
#    - При кожному переміщенні гравця збільшуйте лічильник кроків.  
#    - Реалізуйте функцію `move(direction)`, яка:
#      - Перевіряє, чи доступний вибраний напрямок з поточної кімнати.
#      - Оновлює значення `поточна_кімната` та збільшує лічильник кроків.
#      - Кожні 10 кроків викликає функцію `refresh_rooms()`, яка оновлює вміст усіх кімнат (крім `"вхід"` та `"скарбниця"`).
#    - Функція `check_room(room)` повинна обробляти події залежно від вмісту:
#      - Якщо знайдено `"скарб"`, додати 10 очок і змінити вміст кімнати на `"порожньо"`.
#      - Якщо знайдено `"великий скарб"`, додати 50 очок і змінити вміст кімнати.
#      - Якщо знайдено `"монстр"`, завдати випадкову шкоду (від 10 до 30) і змінити вміст кімнати.
#      - Якщо знайдено `"здоров'я"`, збільшити здоров’я на випадкове число від 7 до 15 і змінити вміст кімнати.
#      - Якщо кімната порожня, просто повідомити про це.
# 
# 5. Умова перемоги та поразки:  
#    - Перемога: Якщо кількість зібраних скарбів досягає (або перевищує) 70 очок, гра завершується з повідомленням про перемогу.  
#    - Поразка: Якщо здоров’я гравця падає до 0 або нижче, гра завершується з повідомленням про поразку.
# 
# 6. Інтерфейс:  
#    - Гра повинна працювати в циклі, виводячи поточний стан гравця (здоров’я, скарби, поточну кімнату) та список можливих напрямків
#       для руху.
#    - Гравець вводить напрямок (наприклад, `"вперед"`, `"назад"`, `"праворуч"`, `"ліворуч"`), після чого програма оновлює
#       стан гри відповідно до вибраного шляху.
# 
# 7. Додатково:  
#    - Через кожні 10 кроків (перехід між кімнатами) має оновлюватися вміст кімнат за допомогою функції `refresh_rooms()`,
#    що надає нові випадкові події у кімнатах (крім `"вхід"` та `"скарбниця"`).

import random

dungeon = {
    "вхід": {"праворуч": "кімната 1", "вперед": "кімната 2"},
    "кімната 1": {"назад": "вхід", "вперед": "кімната 3"},
    "кімната 2": {"назад": "вхід", "праворуч": "кімната 3"},
    "кімната 3": {"назад": "кімната 1", "ліворуч": "кімната 2", "вперед": "скарбниця"},
    "скарбниця": {"назад": "кімната 2"}
}

room_contents = {
    "вхід": "порожньо",
    "кімната 1": random.choices(["скарб", "монстр", "порожньо", "здоров'я"], weights=[1, 3, 1, 2])[0],
    "кімната 2": random.choices(["скарб", "монстр", "порожньо", "здоров'я"], weights=[1, 3, 1, 2])[0],
    "кімната 3": random.choices(["скарб", "монстр", "порожньо", "здоров'я"], weights=[1, 3, 1, 2])[0],
    "скарбниця": "великий скарб"
}

player = {
    "здоров'я": 100,
    "скарби": 0,
    "поточна_кімната": "вхід"
}

steps_count = 0

def show_status():
    print(f"\nЗдоров'я: {player["здоров'я"]} | Скарби: {player["скарби"]}")
    print(f"Ви в {player["поточна_кімната"]}")

    available_directions = dungeon[player["поточна_кімната"]]
    if available_directions:
        print(f"Можливі напрямки {', '.join(available_directions.keys())}")
    else:
        print("Немає виходів з цієї")

    print("Доступні кімнати " + ", ".join(dungeon.keys()))

def refresh_rooms():
    global room_contents
    for room in room_contents:
        if room not in ['вхід', "скарбниця"]:
            room_contents[room] = random.choices(["скарб", "монстр", "порожньо", "здоров'я"], weights=[1, 3, 1, 2])[0]
    print("\n Вміст кімнат оновлено!")

def check_victory():
    if player["скарби"] >= 70:
        print("Вітаю! Перемога!")
        exit()

def move(direction):
    global steps_count
    current_room = player["поточна_кімната"]
    if direction in dungeon[current_room]:
        new_room = dungeon[current_room][direction]
        player["поточна_кімната"] = new_room

        steps_count += 1
        if steps_count % 10 == 0:
            refresh_rooms()

        check_room(new_room)
    else:
        print("Туди йти не можна")

def check_room(room):
    content = room_contents[room]

    if content == "скарб":
        print("Ви знайшли скарб! +10")
        player["скарби"] += 10

        room_contents[room] = "порожньо"
        check_victory()

    elif content == "монстр":
        damage = random.randint(10, 30)
        print(f"Напад монстра -{damage}")
        player["здоров'я"] -= damage
        room_contents[room] = "порожньо"

        if player["здоров'я"] <= 0:
            print("Здоров'я <= 0. Гру завершено!")
            exit()

    elif content == "великий скарб":
        print("Ви знайшли великий скарб! +50")
        player["скарби"] += 50

        room_contents[room] = "порожньо"
        check_victory()

    elif content == "здоров'я":
        bonus = random.randint(7, 15)
        print(f"Ви знайшли лікування!  +{bonus}")
        player["здоров'я"] += bonus
        room_contents[room] = "порожньо"

    else:
        print("Тут порожньо")

def game():
    print("Доступні кімнати " + ", ".join(dungeon.keys()))
    while True:
        show_status()
        direction = input("\nКди йдемо? (вперед/назад/праворуч/ліворуч): ").strip().lower()
        move(direction)

game()



