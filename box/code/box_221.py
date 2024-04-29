import matplotlib.pyplot as plt
import numpy as np

data =[["Bakery",[2,6,10,14,18],[30]],
    ["Beverages",[1,3,5,7,9],[11,15]],
    ["Meat",[6,14,22,30,38],[50,55]],
    ["Dairy",[1.5,3,4.5,6,7.5],[13,15]],
    ["Snacks",[0.8,2,3.2,4.4,5.6],[7.8,10]]]

boxData = [item[1] for item in data]
outlierData = [item[2] for item in data]
labels = [item[0] for item in data]

# Create the figure and add the box plot
fig = plt.figure(figsize=(10,6)) 
ax = fig.add_subplot(111)
bp = ax.boxplot(boxData, notch=True, vert=1, patch_artist=True, labels=labels, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'red', 'yellow']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Calculate and plot outliers manually
for i, outlier in enumerate(outlierData):
    if outlier:
        x = [i + 1] * len(outlier)
        ax.plot(x, outlier, 'kx')
        
# Applying grid
ax.yaxis.grid(True)
ax.xaxis.grid(True)

# Set the title and labels
plt.xlabel('Product Category')
plt.ylabel('Price ($)')
plt.title('Price Distribution in Different Food and Beverage Categories (2021)')

# Applying tight layout before saving the figure
plt.tight_layout()

# Save the figure in specified path
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/172_202312310058.png')

# Clear the current figure
plt.clf()
