import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

x = 10000
p = 0.5
size = 10_000
y = rng.binomial(x, p, size)

plt.hist(y, bins=500)
plt.show()
