import random
from unidecode import unidecode

# Список відомих людей для гри
people = [
    {
        "name": "Марія Кюрі",
        "hints": [
            "Ця жінка народилася в 20 столітті.",
            "Вона отримала Нобелівську премію.",
            "Ця жінка відома своїми науковими досягненнями."
        ]
    },
    {
        "name": "Альберт Ейнштейн",
        "hints": [
            "Ця особа народилася в Німеччині.",
            "Він відомий своєю теорією відносності.",
            "Він отримав Нобелівську премію з фізики."
        ]
    },
    {
        "name": "Леонардо да Вінчі",
        "hints": [
            "Ця людина жила в епоху Відродження.",
            "Він був художником і винахідником.",
            "Його картина 'Мона Ліза' відома у всьому світі."
        ]
    }
]

# Функція для перевірки вводу
def check_input(user_input, correct_name):
    # Перетворюємо ввід та правильне ім'я в одну форму (без акцентів)
    user_input_normalized = unidecode(user_input.lower())
    correct_name_normalized = unidecode(correct_name.lower())
    
    if user_input_normalized == correct_name_normalized:
        return True
    return False

# Функція для перевірки вводу користувача
def is_valid_input(user_input):
    # Перевіряємо, чи ввід складається тільки з букв і пробілів
    return all(c.isalpha() or c.isspace() for c in user_input)

# Основна логіка гри
def play_game():
    print("Ласкаво просимо до гри 'Це відома людина чи ні?'")
    print("Я загадав відому людину, і ваша задача — вгадати, хто це.")

    # Вибір випадкової відомої особи
    person = random.choice(people)
    name = person["name"]
    hints = person["hints"]
    attempts = 0
    max_attempts = 4

    # Підказки з'являються поступово
    while attempts < max_attempts:
        user_input = input(f"Спроба {attempts + 1}. Введіть ваше припущення: ")

        # Перевірка некоректного вводу
        if not is_valid_input(user_input):
            print("Помилка! Введіть лише букви та пробіли.")
            continue

        # Перевірка на правильність
        if check_input(user_input, name):
            print("Ого! Ви вгадали! Це справжній переможець!")
            break
        else:
            attempts += 1
            print("Неправильно. Спробуйте ще раз.")
            # Підказка після кожної невдалої спроби
            if attempts <= len(hints):
                print(f"Підказка: {hints[attempts - 1]}")

    if attempts == max_attempts and not check_input(user_input, name):
        print(f"Гра завершена. Ви не вгадали. Це була {name}.")
        
# Запуск гри
play_game()
