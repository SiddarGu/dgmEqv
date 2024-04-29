
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[60,80,90,95,99], [75,85,90,95,98], [50,70,85,90,95], [70,80,85,90,95], [60,75,85,95,98]]
outliers = [[], [100,102], [110,112], [100,101], [99,102]]

# Plot the data with the type of box plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)

# Outliers are plotted manually using ax.plot for each category
for i, outlier in enumerate(outliers):
    if outlier:
        x = [i + 1] * len(outlier)
        ax.plot(x, outlier, 'ro')

# Adjust the parameters
ax.set_title('Efficiency Ranking of Government Agencies in 2021')
ax.set_xlabel('Government Agency')
ax.set_ylabel('Efficiency (%)')
ax.set_xticklabels(['Federal Agency', 'State Agency', 'Local Agency', 'County Agency', 'Municipal Agency'])

# Add background grids
ax.grid(linestyle='--', alpha=0.3)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/22_202312270030.png')

# Clear the current image state
plt.clf()