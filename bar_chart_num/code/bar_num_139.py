
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[260, 450], [90, 200], [80, 180], [105, 230]])
country = ["USA", "UK", "Germany", "France"]

plt.figure(figsize=(10, 6))
ax = plt.subplot(111)
ax.bar(country, data[:, 0], width=0.5, label="Internet Users (million)")
ax.bar(country, data[:, 1], width=0.5, bottom=data[:, 0], label="Data Consumption (GB)")
ax.legend(loc="upper left")
plt.title("Internet users and data consumption in four countries in 2021")
for i, v in enumerate(data[:, 0]):
    ax.text(i, v/2, str(v), color="white", fontsize=14,
            horizontalalignment="center", fontweight="bold")
for i, v in enumerate(data[:, 1]):
    ax.text(i, v + data[:, 0][i]/2, str(v), color="white", fontsize=14,
            horizontalalignment="center", fontweight="bold")
plt.xticks(country)
plt.tight_layout()
plt.savefig('Bar Chart/png/429.png', transparent=True,
            bbox_inches='tight', pad_inches=0.2)
plt.clf()