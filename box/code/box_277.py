import matplotlib.pyplot as plt
import numpy as np

# Given data
data = {"Region": ["North America", "Europe", "Asia", "Africa", "Australia"],
        "Min Emission (Metric Tons)": [500, 600, 550, 400, 480],
        "Q1 Emission (Metric Tons)": [1000, 1200, 1100, 900, 980],
        "Median Emission (Metric Tons)": [2000, 2300, 2100, 1800, 2000],
        "Q3 Emission (Metric Tons)": [3000, 3500, 3100, 2700, 2900],
        "Max Emission (Metric Tons)": [4000, 4600, 4200, 3700, 3900],
        "Outlier Emission (Metric Tons)": [[6000], [1, 7000], [5000], [4500], [5000, 6000]]}

# Restructure data.
emissions = [list(data[key][i] for key in data.keys() if 'Emission' in key and 'Outlier' not in key) for i in range(len(data["Region"]))]
outliers = data["Outlier Emission (Metric Tons)"]

# Create figure and subplot.
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Boxplot.
bp = ax.boxplot(emissions, patch_artist=True, whis=1.5, vert=0)

# Plot outliers.
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

# Set y-axis labels (rotate if too long).
ax.set_yticklabels(data["Region"], rotation=30)

# Set title and y-label.
ax.set_title('CO2 Emission Distribution by Regions in 2022')
ax.set_ylabel('Metric Tons')

# Enable background grid.
ax.grid(True)

# Save figure.
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/124_202312270030.png')

# Clear figure
plt.clf()
