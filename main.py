def choose_yes_no(question):
    while True:
        response = input(question).strip().lower()
        if response in {"да", "нет"}:
            return response
        print("Пожалуйста, выберите 'Да' или 'Нет'.")

age = choose_yes_no("Вы достигли совершенолетия? Напишите: Да или Нет ").capitalize()
    # (int(input("Введите ваш возраст: ")))

citizenship = choose_yes_no("\nЯвляетесь ли вы гражданином РФ? Напишите: Да или Нет ").capitalize()


limitations = choose_yes_no("\nЕсть ли у вас судимости либо другие ограничения для участия "
                            "в голосовании на выборах? Напишите: Да или Нет ").capitalize()


if age == "Да" and citizenship == "Да" and limitations == "Нет":
    print("\nВы можете участвовать в голосовании.")
else:
    print("\nВы не можете участвовать в голосовании.")