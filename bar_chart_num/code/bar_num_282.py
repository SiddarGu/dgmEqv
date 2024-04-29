
import matplotlib.pyplot as plt
import numpy as np

# data
country = ["USA", "UK", "Germany", "France"]
fruit_production = [2000, 2500, 1800, 2300]
vegetables_production = [4000, 4500, 3800, 4700]

# figure size
plt.figure(figsize=(9, 6))

# position of the legend
ax = plt.subplot(111)

# plot bar charts
ax.bar(country, fruit_production, width = 0.2, label="Fruit Production", color="green")
ax.bar(country, vegetables_production, width = 0.2, bottom=fruit_production, label="Vegetables Production", color="red")

# title
plt.title("Fruit and vegetables production in four countries in 2021")

# legend
ax.legend(loc="upper left")

# add grid
ax.grid(axis="y")

# add value of every bar
for i in range(len(country)):
    ax.annotate(str(fruit_production[i]), xy=(i-0.2,fruit_production[i]+200))
    ax.annotate(str(vegetables_production[i]), xy=(i+0.2,vegetables_production[i]+200))

# set x ticks
plt.xticks(np.arange(len(country)), country, rotation=45, ha="right")

# adjust the figure size and spacing
plt.tight_layout()

# save image
plt.savefig("Bar Chart/png/8.png")

# clear figure
plt.clf()