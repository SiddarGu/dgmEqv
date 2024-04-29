
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data 
data = {
    "Household": [5, 20, 30, 40, 50],
    "Transportation": [30, 60, 90, 120, 150],
    "Industrial": [50, 100, 150, 200, 250],
    "Agriculture": [20, 40, 60, 80, 100],
    "Waste": [10, 30, 50, 70, 90]
}
outliers = {
    "Transportation": [180],
    "Agriculture": [150],
    "Waste": [100]
}

# Plot the data with the type of box plot
fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(111)
ax.grid(True, linestyle = '-.')
data_plot = [data[key] for key in data.keys()]
ax.boxplot(data_plot, labels=list(data.keys()), patch_artist=True)

# Plot the outliers
for i, key in enumerate(outliers.keys()):
    if len(outliers[key]) > 0:
        ax.plot([i + 1] * len(outliers[key]), outliers[key], 'bx')

# Titles and labels
ax.set_title('Carbon Footprint Distribution in 2021')
ax.set_ylabel('Carbon Footprint (kgCO2)')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/1_202312251315.png')

# Clear the current image state
plt.clf()