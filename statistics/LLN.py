# Law of Large Numbers
# 大数の法則

import matplotlib.pyplot as plt
import seaborn as sns
from random import randint

sns.set_theme(style="whitegrid")

MAX = 1_000

a = []
b = []

for _ in range(MAX):
    a.append(randint(1, 6))
    b.append(sum(a) / len(a))

sns.lineplot(x=[0, MAX], y=[3.5, 3.5], linewidth=3)
p = sns.lineplot(x=range(MAX), y=b, linewidth=3)

p.set_title("Average dice roll by number of rolls")
p.set_xlim(0, MAX)
p.set_ylim(1, 6)
p.set_xlabel("Number of trials")
p.set_ylabel("μ")

plt.show()
