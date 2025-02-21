try:
    text = input("Введите строку: ")
    if not text.isalpha():
        raise ValueError("Ошибка! Вводите только буквы.")
    print("Всё хорошо! Вы ввели:", text)
except ValueError as e:
    print(e)
