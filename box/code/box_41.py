
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[2.5, 4.2, 5.7, 7.4, 9.2], 
        [3.5, 5.5, 7.2, 8.7, 10.2], 
        [2.0, 4.2, 6.1, 7.8, 9.2],
        [4.5, 6.2, 7.9, 9.5, 11.3],
        [3.2, 5.3, 7.0, 8.9, 10.2]]
outliers = [[], [14.5], [1.2, 12.5, 14.5], [13.0, 14.2], [13.5]]

# Plot the data with the type of box plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)

# Plot the outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'o', markersize=6, color='blue')

# Draw background grids
ax.grid(linestyle='--', alpha=0.5)

# Set labels
ax.set_xticklabels(['Country A', 'Country B', 'Country C', 'Country D', 'Country E'], fontsize=10)
ax.set_ylabel('Emission (Tonnes)', fontsize=10)

# Set title
ax.set_title('Greenhouse Gas Emission Distribution in Different Countries (2021)', fontsize=14)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/44_202312270030.png')

# Clear the current image state
plt.clf()