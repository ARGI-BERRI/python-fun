import matplotlib.pyplot as plt
import seaborn as sns
from random import randint

sns.set_theme()

n = 5
a = [sum([randint(1, 6) for _ in range(n)]) / n for _ in range(1000)]

p = sns.histplot(a, binwidth=0.2)
p.set_title(f"Trials: {n}")
p.set_xlim(1, 6)
plt.show()
