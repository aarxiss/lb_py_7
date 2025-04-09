import random
import time

# Список можливих об'єктів, які можна вгадати
objects = [
    {"name": "молоко", "category": "речовина"},
    {"name": "кіт", "category": "тварина"},
    {"name": "Ейнштейн", "category": "людина"},
    {"name": "машина", "category": "транспорт"},
    {"name": "місяць", "category": "небесне тіло"},
    {"name": "стіл", "category": "речовина"}
]

# Функція для випадкових підказок
def give_hint(correct_name, attempts):
    # Випадкова підказка: правильна або неправильна
    hints = [
        f"Це {correct_name}, але, можливо, і не зовсім.",
        f"Виглядає, як {correct_name}, але це може бути щось інше.",
        "Це те, що ви шукаєте, хоча, можливо, це й не так.",
        "Це точно {correct_name}, чи не так?",
        "Не зовсім те, що ви думаєте, але набагато цікавіше!"
    ]
    # Іноді ми повертаємо неправильну підказку
    if random.choice([True, False]):
        return random.choice(hints)
    else:
        return f"Це точно {correct_name}!"

# Функція для перевірки вводу
def check_input(user_input, correct_name):
    if user_input.lower() == correct_name.lower():
        return True
    return False

# Основна логіка гри
def play_game():
    print("Ласкаво просимо до гри 'Я думаю, це... хоча, може, й ні!'")
    print("Виберіть, що ви хочете вгадати. Можливо, вам навіть не повідомлять, що саме.")
    
    # Гравець вибирає категорію для вгадування
    print("Категорії: 'речовина', 'тварина', 'людина', 'транспорт', 'небесне тіло'")
    category = input("Введіть категорію для вгадування: ").lower()
    
    # Вибір об'єкта в залежності від категорії
    possible_objects = [obj for obj in objects if obj["category"] == category]
    if not possible_objects:
        print("Ой! Ця категорія порожня. Обирайте іншу.")
        return

    chosen_object = random.choice(possible_objects)
    correct_name = chosen_object["name"]
    attempts = 0

    print(f"Ви вибрали категорію '{category}'. Починаємо грати!")

    while True:
        user_input = input(f"Спроба {attempts + 1}: Введіть вашу відповідь: ")

        # Якщо ввід некоректний
        if not user_input.isalpha() and not user_input.isspace():
            print("О, здається, ви ввели щось непотрібне. Спробуйте знову!")
            continue

        # Перевірка на правильність
        if check_input(user_input, correct_name):
            print("Може, ви і не розумієте, як ви це зробили, але ви виграли!")
            break
        else:
            attempts += 1
            hint = give_hint(correct_name, attempts)
            print(f"Підказка: {hint}")

        # Завершення гри в абсолютно випадковий момент
        if random.choice([True, False]):
            print("Гра завершується... чи виграли ви? Це питання не таке очевидне.")
            break

# Запуск гри
play_game()
