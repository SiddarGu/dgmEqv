
import matplotlib.pyplot as plt
import numpy as np

data = {"Country":["USA", "UK", "Germany", "France"],
        "Economics(%)":[40, 35, 37, 38],
        "Sociology(%)":[20, 25, 22, 21],
        "Psychology(%)":[30, 35, 32, 39]
       }

x = np.arange(len(data["Country"]))
width = 0.2

fig, ax = plt.subplots(figsize=(14, 7))

ax.bar(x-width, data["Economics(%)"], width=width, label="Economics(%)", color="red")
ax.bar(x, data["Sociology(%)"], width=width, label="Sociology(%)", color="green")
ax.bar(x+width, data["Psychology(%)"], width=width, label="Psychology(%)", color="blue")

ax.set_ylabel("percentage")
ax.set_title("Percentage of Social Sciences and Humanities in four countries in 2021")
ax.set_xticks(x)
ax.set_xticklabels(data["Country"])
ax.legend()

for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.annotate(str(i.get_height()), (i.get_x() + i.get_width() / 2., i.get_height() + 0.5),
                ha="center", va="bottom", rotation=0)

plt.tight_layout()
plt.savefig("Bar Chart/png/86.png")
plt.clf()