import matplotlib.pyplot as plt
import numpy as np 

# Provided data
categories = ['Energy Consumption (KWh)', 'Water Consumption (Gallons)', 'Waste Production (Kg)', 'Carbon Footprint (Tons)', 'Renewable Energy Usage (%)']
box_data = [[200, 400, 600, 800, 1000], 
            [1000, 2000, 3000, 4000, 5000], 
            [100, 200, 300, 400, 500],
            [10, 20, 30, 40, 50], 
            [5, 15, 25, 35, 45]]
outliers = [[], 
            [8000], 
            [25, 700], 
            [75],
            [55]]

# Creating the boxplot
fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(box_data, whis=1.5, patch_artist=True)

# Customizing boxplot colors
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightpink', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plotting outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'x')

# Setting labels and title
ax.set_xticklabels(categories, rotation=30, ha='right')
ax.set_ylabel('Values')
plt.title('Sustainability Indicators Distribution (2022)')
plt.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Tight layout for better spacing
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/241_202312310058.png')
plt.clf()
