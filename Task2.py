res = ""
a = input("Введите слово (для завершения используйте stop): ")
if a.lower() == "stop":
    print("Вы не ввели ни одного слова!")
else:
    while a.lower() != "stop":
        res += a + " "
        a = input("Введите слово (для завершения используйте stop): ")

    print(f"Результат: {res}")