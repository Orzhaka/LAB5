import random

da = 0
net = 0

while da <3 and net < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print(f"{num1} + {num2} = ")
    a = int(input())
    if a == num1 + num2:
        print("Правильно!")
        da += 1
    else:
        print("Ответ неверный")
        net += 1
        da = 0
else:
    if da == 3:
        print(f"Поздравляем, вы победили! Игра окончена. Ошибок: {net}")
    elif net == 3:
        print(f"Игра окончена. Правильных ответов: {da}")
