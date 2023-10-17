import seaborn as sns
import matplotlib.pyplot as plt
from lib.pmf import bernoulli

sns.set_theme(style="whitegrid")

pmf1 = [bernoulli(20, 0.5, k) for k in range(1, 20)]
pmf2 = [bernoulli(20, 0.7, k) for k in range(1, 20)]
pmf3 = [bernoulli(40, 0.5, k) for k in range(1, 40)]

p = sns.scatterplot(x=range(1, 20), y=pmf1, s=30)
p = sns.scatterplot(x=range(1, 20), y=pmf2, s=30)
p = sns.scatterplot(x=range(1, 40), y=pmf3, s=50)

plt.xlabel("k")
plt.ylabel("probability")

plt.show()
