# Example demonstrating box plots


import matplotlib.pyplot as plt
import numpy as np

foo = 23
np.random.seed(foo)
ds_no_1 = np.random.normal(10, foo, 200)
ds_no_2 = np.random.normal(90, 20, 200)
ds_no_3 = np.random.normal(80, 30, 200)
ds_no_4 = np.random.normal(70, 40, 200)
d = [ds_no_1, ds_no_2, ds_no_3, ds_no_4]

fig = plt.figure(figsize=(foo, 7))
ax = fig.add_subplot(111)

bp = ax.boxplot(d, patch_artist=True, notch="True", vert=0)

colz = ["#0000FF", "#00FF00", "#FF0000", "#FFF000"]

for patch, color in zip(bp["boxes"], colz):
    patch.set_facecolor(color)

for whisker in bp["whiskers"]:
    whisker.set(color="#23008B", linewidth=1.5, linestyle=":")

# changing color and linewidth of
for cap in bp["caps"]:
    cap.set(color="#23008B", linewidth=2)

for median in bp["medians"]:
    median.set(color="red", linewidth=5)

# changing style of fliers
for flier in bp["fliers"]:
    flier.set(marker="D", color="#e7298a", alpha=0.5)

ax.set_yticklabels(["ds_no_1", "ds_no_2", "ds_no_3", "ds_no_4"])

plt.title("Example of customized box plots")

ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

plt.show()
