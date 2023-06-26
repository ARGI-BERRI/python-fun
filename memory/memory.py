import os
import random
from time import sleep
from typing import List

# Remembering configuration
REMEMBER_COUNT = 3
REMEMBER_WAIT = 1

# Range of random values
RANDOM_MIN = 1
RANDOM_MAX = 100

# Magic Numbers
INTERVAL = 1

# GLOBAL VARIABLE (fuck)
memory: List[int] = []
correct = 0


def main() -> None:
    run_opening()

    # GO GO GO
    run_calculating()

    run_ending()


def run_opening() -> None:
    """
    This function runs the opening process.
    """

    # Clear the console before starting
    clear_console()

    print("Press Enter to continue...", end="")
    input()

    # 3...2...1...
    for i in range(3, 0, -1):
        print(f"{i}...")
        sleep(INTERVAL)


def run_calculating() -> None:
    """
    This function runs the main calculating process.
    """

    global correct
    global memory

    # Clear the console
    clear_console()

    for _ in range(REMEMBER_COUNT):
        num = random.randrange(RANDOM_MIN, RANDOM_MAX)
        memory.append(num)

        print(num)
        sleep(REMEMBER_WAIT)

        clear_console()

    correct = sum(memory)


def run_ending() -> None:
    """
    This function runs the ending.
    """

    # Verifing if input is castable into int
    while True:
        try:
            print("Your answer is: ", end="")
            answer = int(input())
            break

        except ValueError:
            print("FUCK! INPUT THE INTEGER!")

    if answer == correct:
        print("YOU ARE GENIOUS")
    else:
        print(f"YOU ARE NOT SO CLEVER. ANSWER IS: {correct}")

    print(f"MEMORY DATA WAS {memory} .")


def clear_console():
    if os.name == "nt":
        os.system("cls")
    # TODO: Not tested, so need to run on GNU/Linux
    elif os.name == "posix":
        os.system("clear")
    # TODO: Are there something else other than Windows or POSIX system?!
    else:
        print("YOUR OS NOT SUPPORTED! FUCK!")
        exit()


if __name__ == "__main__":
    main()
