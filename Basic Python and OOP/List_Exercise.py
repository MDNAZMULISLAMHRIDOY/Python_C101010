import matplotlib.pyplot as plt
import numpy as np

scores = np.random.normal(loc=2, scale=2, size=1000)

plt.hist(scores)
plt.show()