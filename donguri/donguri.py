import asyncio
import os

CROTCHET = 0.3  # 四分音符
QUAVER = CROTCHET / 2  # 八分音符
METRE = CROTCHET * 4  # 一小節


class Note:
    def __init__(self, lyric: str, timing: float) -> None:
        self.lyric = lyric
        self.timing = timing


notes = [
    # どんぐりころころ
    Note("ど", METRE * 0 + CROTCHET * 0),
    Note("ん", METRE * 0 + CROTCHET * 1),
    Note("ぐ", METRE * 0 + CROTCHET * 2),
    Note("り", METRE * 0 + CROTCHET * 3),
    Note("こ", METRE * 1 + CROTCHET * 0),
    Note("ろ", METRE * 1 + CROTCHET * 1),
    Note("こ", METRE * 1 + CROTCHET * 2),
    Note("ろ", METRE * 1 + CROTCHET * 3),
    Note("　", METRE * 1 + CROTCHET * 3),
    # どんぐりこ
    Note("ど", METRE * 2 + CROTCHET * 0),
    Note("ん", METRE * 2 + CROTCHET * 1),
    Note("ぐ", METRE * 2 + CROTCHET * 2),
    Note("り", METRE * 2 + CROTCHET * 3),
    Note("こ", METRE * 3 + CROTCHET * 0),
]


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


async def play(note: Note):
    await asyncio.sleep(note.timing)
    print(note.lyric, end="")


async def main():
    clear_console()

    async with asyncio.TaskGroup() as tg:
        [tg.create_task(play(note)) for note in notes]


# あんた行く
asyncio.run(main())
