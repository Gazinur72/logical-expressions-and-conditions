try:
    print("Введите ваш возраст.")
    age = int(input())

    print("""\nЯвляетесь ли вы гражданином РФ? 1 - Да2 - Нет""")
    citizenship = int(input())

    if citizenship == 1:
        print("Вы выбрали 'Да'\n")
    elif citizenship == 2:
        print("Вы выбрали 'Нет'\n")
    else:
        print("Выберите 1 или 2")

    print("""\nЕсть ли у вас судимости либо другие ограничения для участия в голосовании на выборах?1 - Да2 - Нет""")

    limitations = int(input())
    if limitations == 1:
        print("Вы выбрали 'Да'")
    elif limitations == 2:
        print("Вы выбрали 'Нет'")
    else:
        print("Выберите 1 или 2")

    if age >= 18 and citizenship == 1 and limitations == 2:
        print("\nВы можете участвовать в голосовании.")
    else:
        print("\nВы не можете участвовать в голосовании.")
except ValueError:
    print("Ошибка. Введите, пожалуйста, ответ цифрами.")
