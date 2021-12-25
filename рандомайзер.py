import random 
random_value = random.randint(0, 20)
attempt = 0
print ("Компьютер зашадал число от 0 до 20, и у вас 3 попытки, чтобы отгадать его")
for i in range(20):
    choise = int(input("Введите число: "))
    if choise > random_value:
        print('много')

    elif choise < random_value:
        print('мало')

    else:
        print(f"Вы угадали чсило с {i} попытки")
        break 
    attempt += 1

    if attempt >=3:
        print(f"Вы исчерпали свои 3 попытки! Загаданное чиало {random_value}")
