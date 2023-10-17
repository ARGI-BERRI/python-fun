import datetime


def main():
    # 生まれ年
    birth_year, birth_month, birth_day = input("format: YYYY/mm/dd : ").split("/")

    # 今年
    dt = datetime.datetime.today()
    this_year = dt.year
    this_month = dt.month
    this_day = dt.day

    # 現在の日付
    current_year = int(birth_year)
    current_month = int(birth_month)
    current_day = int(birth_day)

    elapsed_days = 0

    while this_year >= current_year:
        month_limit = this_month if current_year == this_year else 12
        while month_limit >= current_month:
            day_limit = (
                this_day
                if current_year == this_year and current_month == this_month
                else get_month_len(current_month, is_leap_year(current_year))
            )

            while day_limit >= current_day:
                elapsed_days += 1
                current_day += 1
            # END WHILE DAY

            current_day = 1
            current_month += 1
        # END WHILE MONTH

        current_month = 1
        current_year += 1

    # END WHILE YEAR

    print(elapsed_days)


def is_leap_year(year: int) -> bool:
    # 4 で割り切れないなら平年
    if year % 4 != 0:
        return False

    # 100で割り切れるが400で割り切れないなら平年
    if year % 100 == 0 and year % 400 != 0:
        return False

    return True


def get_month_len(month: int, leap_year=False) -> int:
    if leap_year and month == 2:
        return 29

    #        1   2   3   4   5   6   7   8   9  10  11  12
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]


main()
