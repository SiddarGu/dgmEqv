
import matplotlib.pyplot as plt
import numpy as np

# set figure
fig = plt.figure(figsize=(12, 8))

# set data
country = ["USA", "UK", "Germany", "France"]
Engineers = [1300, 1000, 1500, 1200]
Researchers = [1800, 1400, 1800, 1500]

# set x, y, ticks, and title
x = np.arange(len(country))
width = 0.35

# set bar chart
ax = fig.add_subplot(111)
ax.bar(x - width/2, Engineers, width=width, label="Engineers")
ax.bar(x + width/2, Researchers, width=width, label="Researchers")

ax.set_xticks(x)
ax.set_xticklabels(country, rotation=90)
ax.set_title("Number of engineers and researchers in four countries in 2021")

# set legend
ax.legend()

# set grid
ax.grid(True, linestyle='-.')

# set tight layout
plt.tight_layout()

# save image
plt.savefig("bar chart/png/198.png")

# clear figure
plt.clf()