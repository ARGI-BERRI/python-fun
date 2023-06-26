import os
import random
import requests
import time


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class TypingGame:
    DICTIONARY_URL = "https://www.mit.edu/~ecprice/wordlist.10000"

    def __init__(self, word_min=1, word_max=20) -> None:
        self.WORD_LENGTH_MAX = word_max
        self.WORD_LENGTH_MIN = word_min

        self.match_count = 0
        self.time_start = time.time()

        self.words = self.init_words()
        self.word = random.choice(self.words)
        self.hints = self.init_hints()

    def init_words(self) -> list[str]:
        """単語リストを外部から取得し、それを返却する

        Returns:
            list[str]: 単語リスト
        """
        if not os.path.isfile("data/wordlist.txt"):
            url = self.DICTIONARY_URL
            text = requests.get(url).content.decode()

            with open("data/wordlist.txt", "w") as f:
                f.write(text)

        with open("data/wordlist.txt", "r") as f:
            words = list(
                filter(
                    lambda text: self.WORD_LENGTH_MAX
                    > len(text)
                    > self.WORD_LENGTH_MIN,
                    f.read().split("\n"),
                )
            )

            return words

    def init_hints(self) -> list[str]:
        """ヒントリストを生成する

        Returns:
            list[str]: ヒントリスト
        """
        hint_with_head = self.word[0] + "*" * (len(self.word) - 1)
        hint_wo_middle = self.word[0] + "*" * (len(self.word) - 2) + self.word[0 - 1]
        return [
            f"ANSWER IS {hint_with_head}",
            f"ANSWER IS {hint_wo_middle}",
            f"FINAL HINT: {self.anonymize(self.word)}",
        ]

    def time_passed(self) -> float:
        """経過時間を返す

        Returns:
            float: 経過時間（秒）
        """
        return round(time.time() - self.time_start, 2)

    def is_match(self, guess: str) -> bool:
        self.match_count += 1
        return guess == self.word

    def get_matches(self, guess: str) -> tuple[int, str]:
        chars = "".join(
            [
                guess[i] if guess[i] == self.word[i] else "*"
                for i in range(min(len(guess), len(self.word)))
            ]
        ).ljust(len(self.word), "*")[: len(self.word)]

        return len(chars) - chars.count("*"), chars

    def get_hint(self) -> str:
        if self.hints:
            self.match_count += 1
            return self.hints.pop(0)
        else:
            return "NO HINTS AVAILABLE. SENDING %exit TO SURRENDER."

    @staticmethod
    def anonymize(text: str) -> str:
        return "".join([text[i] if i % 2 == 0 else "*" for i in range(len(text))])

def main():
    clear_console()

    game = TypingGame()

    print("WORD MATCHER V.666")
    print("(C) 2023 ARGIA ALL RIGHTS RESERVED.")
    print("SEND %help to SHOW THE HELP.")
    print("")

    print(f"WORD LENGTH IS {len(game.word)}. HOPE YOU WIN.")

    while True:
        try:
            guess = input(f"[{game.match_count}] YOU GUESS: ")

            if not guess:
                continue

            if guess == "%hint":
                print(game.get_hint())
                continue

            if guess == "%time":
                print(f"{game.time_passed()}s ELAPSED")
                continue

            if guess == "%help":
                print("SEND %hint TO EARN HINTS.")
                print("SEND %time TO GET ELAPSED TIME.")
                print("SEND %surrender TO SURRENDER.")
                continue

            if guess == "%surrender":
                print("YOU ARE NOT SO CLEVER")
                print(f"ANSWER WAS {game.word} ({game.time_passed()}s ELAPSED)")
                break

            if guess == "%quit" or guess == "%exit":
                print("PLEASE USE %surrender INSTEAD")
                continue

            if guess[0] == "%":
                print("UNKNOWN COMMAND. %help IS YOUR FRIEND.")
                continue

            if game.is_match(guess):
                print("YOU ARE GENIOUS")
                print(
                    f"YOU GUESSED {game.match_count} TIMES ({game.time_passed()}s ELAPSED)"
                )
                break
            else:
                count, chars = game.get_matches(guess)
                print(f"NOT COLLECT. MATCHED: {chars} ({count} CHARS)\n")

        except KeyboardInterrupt:
            print("ABORTING......")
            return


main()
