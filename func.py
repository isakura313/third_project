import random


def square(x):
    y = random.randint(0, x)
    z = x + y
    print(z ** 2)


for i in range(10):
    square(i)
