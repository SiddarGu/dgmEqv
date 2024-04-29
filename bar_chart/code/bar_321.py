
import matplotlib.pyplot as plt
import numpy as np

# set figsize
plt.figure(figsize=(10, 6))

# set data
Country = ["USA", "UK", "Germany", "France"]
Literature = [450, 400, 380, 430]
Philosophy = [600, 650, 620, 670]
History = [500, 550, 520, 570]

# draw bar chart
x = np.arange(4)
width = 0.2
ax = plt.subplot()
ax.bar(x, Literature, width, label='Literature', color='#4F6228')
ax.bar(x + width, Philosophy, width, label='Philosophy', color='#E7C610')
ax.bar(x + width * 2, History, width, label='History', color='#8B572A')

# add title, xticks, legend, grids
ax.set_title("Number of publications in social sciences and humanities in four countries in 2021")
ax.set_xticks(x + width)
ax.set_xticklabels(Country, rotation=45, ha="right", wrap=True)
ax.legend()
ax.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)

# adjust figure
plt.tight_layout()

# save figure
plt.savefig('bar chart/png/213.png')

# clear figure
plt.clf()