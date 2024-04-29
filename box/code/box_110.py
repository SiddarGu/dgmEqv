import matplotlib.pyplot as plt
import numpy as np

# Restructure the data
categories = ["Electronics", "Apparel", "Home & Kitchen", "Books", "Sports & Outdoors"]
data_list = [[50,550,1100,1500,2000],[30,300,800,1250,2000],[100,600,1100,1750,2500],[80,350,700,1250,1800],[20,200,500,900,1400]]
outliers_list = [[], [20, 2300], [2700], [2200], [10, 1600]]

# Create figure
figure = plt.figure(figsize=(10,8))
ax = figure.add_subplot(111)

# Box plot
ax.boxplot(data_list, notch=True, patch_artist=True, labels=categories, whis=1.5)

# Plot outliers
for i, outlier in enumerate(outliers_list):
    if outlier: # Only plot if there are outliers
        ax.plot([i + 1] * len(outlier), outlier, "bx")

# Configure axes
ax.xaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_title('Sales Distribution across Product Categories in Retail and E-commerce (2024)')
ax.set_ylabel('Sales (units)')
plt.xticks(rotation=45, ha='right')

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/174_202312310058.png')

# Clear figure
plt.clf()
