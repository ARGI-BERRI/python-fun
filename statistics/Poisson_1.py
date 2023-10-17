import seaborn as sns
import matplotlib.pyplot as plt
from lib.pmf import poisson

sns.set_theme(style="whitegrid")

pmf1 = [poisson(1, k) for k in range(1, 20)]
pmf2 = [poisson(4, k) for k in range(1, 20)]
pmf3 = [poisson(10, k) for k in range(1, 20)]

p = sns.scatterplot(x=range(1, 20), y=pmf1, s=30)
p = sns.lineplot(x=range(1, 20), y=pmf1)
p = sns.scatterplot(x=range(1, 20), y=pmf2, s=30)
p = sns.lineplot(x=range(1, 20), y=pmf2)
p = sns.scatterplot(x=range(1, 20), y=pmf3, s=50)
p = sns.lineplot(x=range(1, 20), y=pmf3)

plt.xlabel("k")
plt.ylabel("probability")

plt.show()
