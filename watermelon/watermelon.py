import numpy as np
import random
from util import clear_console


class Movement:
    def __init__(self, x: int, y: int) -> None:
        if not (-1 <= x <= 1 or -1 <= y <= 1):
            RuntimeError()

        self.x = x
        self.y = y

    @staticmethod
    def zero():
        return Movement(0, 0)


class WaterMelonCrasher:
    """
    This class represents the Watermelon Crashing Game.

    Attributes:
        X_RANGE (int): Range of goal position's X-axis. Actual range is (-X_RANGE ~ X_RANGE).
        Y_RANGE (int): Range of goal position's Y-axis. Actual range is (-Y_RANGE ~ Y_RANGE).
        MOVEMENT_KEYS (str): Acceptable keys
        MOVEMENT (dict): Pairs of key and its movement
    """

    X_RANGE = 3
    Y_RANGE = 3

    MOVEMENT_KEYS = "123456789nsew"
    MOVEMENTS = {
        "1": Movement(-1, -1),
        "2": Movement(0, -1),
        "3": Movement(1, -1),
        "4": Movement(-1, 0),
        "5": Movement(0, 0),
        "6": Movement(1, 0),
        "7": Movement(-1, 1),
        "8": Movement(0, 1),
        "9": Movement(1, 1),
        "n": Movement(0, 1),
        "s": Movement(0, -1),
        "e": Movement(1, 0),
        "w": Movement(-1, 0),
    }

    def __init__(self, x=0, y=0) -> None:
        self.x_pos = x
        self.y_pos = y
        self.x_goal = random.randint(self.X_RANGE * -1, self.X_RANGE)
        self.y_goal = random.randint(self.Y_RANGE * -1, self.Y_RANGE)
        self.win = self.distance() == 0

    def move_direction(self, direction: str) -> bool:
        """
        Move to the give direction for 1 unit.
        If invalid direction is given, no action will occur.

        Args:
            direction (str): Regex([nsew123456789])

        Returns:
            bool: if error occurred
        """
        if direction and direction[0] in self.MOVEMENT_KEYS:
            self.move(self.MOVEMENTS[direction[0]])
            return False

        return True

    def move(self, movement: Movement) -> tuple[int, int]:
        """
        Forward for (x, y) unit.

        Args:
            x (int): Forward unit of X-axis
            y (int): Forward unit of Y-axis

        Returns:
            tuple[int, int]: a pair of the current position
        """
        self.x_pos += movement.x
        self.y_pos += movement.y
        self.win = self.distance() == 0

        return self.x_pos, self.y_pos

    def distance(self) -> float:
        dx = self.x_pos - self.x_goal
        dy = self.y_pos - self.y_goal

        d2 = dx**2 + dy**2
        d = np.sqrt(d2)

        return d

    def get_position(self):
        return (self.x_pos, self.y_pos)

    def get_goal(self):
        return (self.x_goal, self.y_goal)


def main():
    game = WaterMelonCrasher()
    clear_console()

    while True:
        direction = input("Where to go [n|s|e|w] ?: ")
        err = game.move_direction(direction)

        print(game.win)

        if game.win:
            print("YOU ARE GENIOUS")
            return

        if err:
            print(f"Invalid operation: {direction}")

        print(f"You are in {game.get_position()}. {game.distance():.2f} m far.")


main()
