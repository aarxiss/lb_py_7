import random

# Список об'єктів (живі, неживі та вигадані)
objects = [
    {"name": "кіт", "type": "живий"},
    {"name": "собака", "type": "живий"},
    {"name": "дерево", "type": "неживий"},
    {"name": "камінь", "type": "неживий"},
    {"name": "дракон", "type": "вигаданий"},
    {"name": "єдиноріг", "type": "вигаданий"}
]

# Функція для перевірки вводу
def check_input(user_input, correct_object):
    if user_input.lower() == correct_object["name"]:
        return True
    else:
        return False

# Основна логіка гри
def play_game():
    print("Вітаємо у грі 'Хтось або щось'!")
    print("Загадано об'єкт. Ваше завдання — вгадати, що це!")
    
    # Вибір випадкового об'єкта
    correct_object = random.choice(objects)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        user_input = input(f"Спроба {attempts + 1}. Введіть ваше припущення: ")

        # Перевірка вводу
        if not user_input.isalpha():
            print("Помилка! Введіть лише букви.")
            continue
        
        # Перевірка правильності вводу
        if check_input(user_input, correct_object):
            print("Вітаємо! Ви вгадали об'єкт.")
            break
        else:
            attempts += 1
            print("Неправильно! Спробуйте ще раз.")

            # Якщо гравець не вгадав, даємо підказку
            if attempts == 2:
                print(f"Підказка: об'єкт {correct_object['type']}.")
    
    if attempts == max_attempts:
        print(f"Гра закінчена. Ви не вгадали об'єкт. Це був {correct_object['name']}.")

# Запуск гри
play_game()
