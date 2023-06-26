from util import clear_console


class SudokuBoard:
    """数独の盤面を表現するクラス"""

    HORIZONTAL_LINE = "+-------+-------+-------+"

    def __init__(self) -> None:
        self.board = [[0] * 9 for i in range(9)]

    def replace(self, x: int, y: int, a: int) -> bool:
        """盤面の特定座標の値を置換する。

        引数:
            x (int): X座標（1 ≦ a ≦ 9）
            y (int): Y座標（1 ≦ a ≦ 9）
            a (int): 置換先の値（1 ≦ a ≦ 9）

        返り値:
            bool: 置換が成功したか否か
        """
        if not (1 <= x <= 9 and 1 <= y <= 9 and 1 <= a <= 9):
            return False

        try:
            self.board[x - 1][y - 1] = a
        except IndexError:
            return False

        return True

    def get_board(self) -> str:
        board = [
            " ".join(
                ["|"]
                + [str(i) for i in row[0:3]]
                + ["|"]
                + [str(i) for i in row[3:6]]
                + ["|"]
                + [str(i) for i in row[6:9]]
                + ["|"]
            )
            for row in self.board
        ]

        board[3:3] = [self.HORIZONTAL_LINE]
        board[7:7] = [self.HORIZONTAL_LINE]

        return "\n".join([self.HORIZONTAL_LINE] + board + [self.HORIZONTAL_LINE])

    def verify(self) -> bool:
        """数独として完成しているか評価する。

        返り値:
            bool: 完成しているか否か
        """
        return False


class SudokuState:
    OPERATION_OK: bool
    VERIFICATION_OK: bool

    def __init__(self) -> None:
        self.OPERATION_OK = True
        self.VERIFICATION_OK = False

    def reset(self):
        pass


def main():
    board = SudokuBoard()
    state = SudokuState()

    while True:
        clear_console()

        #
        # Phase I: Print the board and its status
        #

        print(board.get_board())

        if state.VERIFICATION_OK:
            print("YOU ARE GENIOUS")
            break
        else:
            print("Verifications is failed")

        if not state.OPERATION_OK:
            print("Operation is not valid")

        #
        # Phase II: Analyze the input
        #

        target = input("<x y value>: ")

        if not target:
            continue

        if target == "%quit" or target == "%exit":
            print("Abort.")
            return

        #
        # Phase III: Replacing the board
        #

        target = target.split(" ")

        try:
            x = int(target[0])
            y = int(target[1])
            value = int(target[2])
        except (ValueError, IndexError):
            state.OPERATION_OK = False
            continue

        state.OPERATION_OK = board.replace(x, y, value)
        state.VERIFICATION_OK = board.verify()


main()
