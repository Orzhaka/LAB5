word = input("Введите слово для проверки на редкость: ")

for i in word:
    if i == "Ф" or i == "ф":
        print("Это редкое слово")
        break
else:
    print("Это не очень редкое слово")