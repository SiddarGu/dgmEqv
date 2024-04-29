
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# data
regions = ['North America', 'Europe', 'Asia', 'South America']
engineers = [2500, 2300, 3000, 2000]
scientists = [1800, 2000, 2200, 1600]

# plot
ax.bar(regions, engineers, label="Engineers", bottom=scientists, color='#1f77b4')
ax.bar(regions, scientists, label="Scientists", color='#ff7f0e')

# labels
ax.set_xlabel("Regions")
ax.set_ylabel("Number of People")

# legend
ax.legend(loc="upper right")

# ticks
plt.xticks(rotation=45)

# title
ax.set_title("Number of Engineers and Scientists in four regions in 2021")

# labels
for x, y in enumerate(engineers):
    ax.annotate(y, (x-0.2, y+300), fontsize=9, ha='center', va='bottom')
for x, y in enumerate(scientists):
    ax.annotate(y, (x-0.2, y+300), fontsize=9, ha='center', va='bottom')

# adjust
plt.tight_layout()

# save
plt.savefig('Bar Chart/png/10.png')

# clear
plt.clf()