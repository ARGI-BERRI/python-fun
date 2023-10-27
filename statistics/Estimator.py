import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style("whitegrid")

MAX = 500
RANGE = 100

# np.random.seed(0)
s = np.random.random(MAX)

m = sum(s) / len(s)
s2 = np.var(s)
estimated_m = [sum(s[0:i]) / i for i in range(1, MAX + 1)]
unbiased_var = [np.var(np.random.choice(s, i), ddof=1)
                for i in range(1, MAX + 1)]

p = sns.lineplot(x=range(0, MAX), y=estimated_m,
                 label="Estimated μ", linewidth=2)
p = sns.lineplot(x=[0, MAX], y=[m, m], label="Real μ", linewidth=2)
p = sns.lineplot(x=range(0, MAX), y=unbiased_var,
                 label="Unbiased variance", color="green", linewidth=2)
p = sns.lineplot(x=[0, MAX], y=[s2, s2], color="green", alpha=0.5, linewidth=2)

p.set(yticks=[0.05 * i for i in range(13)])

plt.show()
