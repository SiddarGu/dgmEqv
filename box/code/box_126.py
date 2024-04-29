
import matplotlib.pyplot as plt
import numpy as np

# Get data from the given string
data = np.array([[30, 90, 150, 210, 300], [45, 75, 130, 190, 280],
                 [60, 120, 180, 240, 320], [15, 60, 100, 140, 200], [20, 50, 90, 130, 170]])
outlier = [[], [1, 400], [10, 15], [300], [320]]

# Generate boxplot
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)

ax.boxplot(data.T, labels=['Clothing Store', 'Grocery Store', 'Electronics Store', 'Home Decor Store', 'Online Store'])
ax.set_title('Price Distribution for Retail and E-commerce in 2021')

for i, o in enumerate(outlier):
    if len(o) > 0:
        x = np.repeat(i + 1, len(o))
        ax.plot(x, o, 'ro', alpha=0.6)

# Prevent string from overwriting
plt.xticks(rotation=45)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/1.png")

# Clear the current image state
plt.cla()