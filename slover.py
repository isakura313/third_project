slovar = {'book': 'книга',
          'table': 'стол',
          'mouse': 'мышка'
          }

slovo = input("Введите слово, попробуем перевести")
if slovo in slovar.keys():
    print(slovar[slovo])
else:
    print("Не может быть! Видимо архивы пусты")


user = {
    'name': "semen",
    'surname': 'semenov',
    'age': 10
}
print(user.items())
for key, value in user.items():
    print(value)

data = {'users': {12: {'name': "semen", 'surname': 'semenov', 'age': 10},
                  13: {'name': "ivan", 'surname': 'ivanov', 'age': 23}}
}