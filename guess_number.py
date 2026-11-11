from random import randint
random_number = randint(1,100)
print('Попробуйте угадать случайное число от 1 до 100')
while True:
    user_input = int(input('Введите число: '))
    if user_input < random_number:
        print('Ваше число меньше того, что загадано')
    elif user_input > random_number:
        print('Ваше число больше того, что загадано')
    else:
        print('Отличная интуиция! Вы угадали число :)')
        break
