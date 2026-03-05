# Example demonstrating box plots


import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

d = np.random.normal(100, 20, 200)
fig = plt.figure(figsize =(13, 11))

print(d)
plt.boxplot(d)
plt.show()

