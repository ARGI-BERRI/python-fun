from random import randint

xp, yp, xg, yg = (0, 0, randint(-3, 3), randint(-3, 3))
a = lambda xp, yp, xg, yg: ((xp - xg) ** 2 + (yp - yg) ** 2) ** 0.5
b = lambda i: [[0, -1], [-1, 0], [1, 0], [0, 1]][int(i / 2) - 1]

while (c := input("IN: ")) and (c := int(c[0])):
    xp, yp = (b(c)[0] + xp, b(c)[1] + yp) if c in [2, 4, 6, 8] else (xp, yp)
    a(xp, yp, xg, yg) == 0 and (print(f"YOU ARE GENIOUS. GOAL: {(xg, yg)}") or exit())
    print(f"{a(xp, yp, xg, yg):.2f} m far. Now: {xp, yp}")
