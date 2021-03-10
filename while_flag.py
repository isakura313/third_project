flag = True

while flag:
    data = input("Введите ваши данные по здоровью")
    if data == 'ill':
        print("Выздоравливайте! Сегодня вы свободны")
        flag = False
    else:
        print("Давай за работу! Через полчаса ответишь снова!")