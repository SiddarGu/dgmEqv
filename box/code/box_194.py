import numpy as np
import matplotlib.pyplot as plt

# Data
companies = ['Company Alpha', 'Company Beta', 'Company Gamma', 'Company Delta', 'Company Epsilon']
values = [[2, 3, 5, 7, 10], [1, 2, 3, 5, 7], [3, 4, 6, 7, 9], [2.5, 3.5, 4.5, 6, 8], [1.5, 2.5, 3.5, 5, 7.5]]
outliers = [[], [0.5, 11], [12, 14], [1.5, 10.5], [0.7, 9]]

# Create figure and add subplot
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

# Create boxplot, adjust parameters and set the whis parameter
bp = ax.boxplot(values, vert=False, widths=0.35, patch_artist=True, medianprops={'linewidth': 2, 'color': 'purple'}, boxprops={'facecolor': 'lightblue', 'edgecolor': 'black', 'linewidth': 1.5}, whiskerprops={'linewidth': 1.5}, capprops={'linewidth': 1.5}, whis=1.5)

# Iterate and plot the outliers for each category
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

# Setting title and labels
plt.title('Delivery Time Distribution across Transportation Companies (2021)')
plt.xlabel('Delivery Time (Days)')
plt.yticks(np.arange(1, len(companies) + 1), companies)

# Enabling grid
ax.grid(True)

# Saving figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/60_202312270030.png')

# Clear figure
plt.clf()
