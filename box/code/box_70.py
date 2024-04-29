import matplotlib.pyplot as plt
import numpy as np

# Restructure the data
artists = ["Artist A", "Artist B", "Artist C", "Artist D", "Artist E"]
art_prices = [[1000, 2000, 3000, 4000, 5000], [2000, 3000, 4000, 5000, 6000], [3000, 4000, 5000, 6000, 7000], [1000, 1500, 2000, 2500, 3000], [1500, 2500, 3500, 4500, 5500]]
outliers = [[], [7500, 10000], [12000, 15000], [4500, 5000], [7000, 8000]]

# Create the figure and axis
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Box plot each category
ax.boxplot(art_prices, vert= False, whis=1.5)

# Plot the outliers
for i, outlier in enumerate(outliers):
    if outlier:
        x = [i + 1] * len(outlier)
        ax.plot(outlier, x, 'r.')

# Customize the plot
plt.yticks(range(1, len(artists) + 1), artists)
ax.set_xlabel("Artwork Price (USD)")
ax.set_title("Artwork Price Distribution Among Different Artists")
ax.grid(True)

# Save figure and clear
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/92_202312270030.png")
plt.cla()
