
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,6))
ax = plt.subplot()

data = {"Country": ["USA", "UK", "Germany", "France"],
        "Number of Corporations": [500, 350, 400, 400],
        "GDP(billion)": [20, 12, 15, 10]}

bars1 = ax.bar(range(len(data["Country"])), data["Number of Corporations"],
               color="r", alpha=0.75,
               label="Number of Corporations", bottom=0)

bars2 = ax.bar(range(len(data["Country"])), data["GDP(billion)"],
               color="b", alpha=0.75,
               label="GDP(billion)", bottom=data["Number of Corporations"])

ax.set_title("Number of Corporations and GDP in four countries in 2021")
ax.set_xticks(range(len(data["Country"])))
ax.set_xticklabels(data["Country"], rotation=-45)
ax.legend()

for bar1, bar2 in zip(bars1, bars2):
    y1 = bar1.get_height()
    y2 = bar2.get_height()
    ax.annotate("%d\n%d" % (y1, y2),
                (bar1.get_x() + bar1.get_width()/2,
                 y1 + y2/2),
                ha="center", va="center",
                size=14, color="k", rotation=-45,
                xytext=(0,7),
                textcoords="offset points")

plt.tight_layout()
plt.savefig("Bar Chart/png/296.png")
plt.clf()