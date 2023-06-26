from os import system
from random import randint
from time import sleep

[(lambda i: [print(f"{i}..."), sleep(1), system("cls")])(i) for i in [3, 2, 1]]
for i in (c := [randint(0, 100), randint(0, 100), randint(0, 100)]):
    (lambda i: [print(i), sleep(1), system("cls")])(i)

print("YOU ARE GENIOUS") if input("Guess: ") == sum(c) else print(f"Answer: {sum(c)}")
