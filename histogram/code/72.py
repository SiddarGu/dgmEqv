import matplotlib.pyplot as plt
import numpy as np

# Given data
data_labels = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
data = [37, 28, 45, 50, 55, 60, 65, 70, 55, 50, 80, 100]
line_labels = ['Monthly Sales ($Million)', 'Number of Retailers']

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the vertical histograms
bars = ax.bar(data_labels, data, color=plt.cm.viridis(np.linspace(0, 1, len(data))))

# Adding grid, title and labels
ax.set_title('Monthly Retail Sales Distribution Among E-commerce Retailers', fontsize=15)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales ($ Million)', fontsize=12)

# Rotate the x-axis labels if they are too long
plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

# Automatically adjust subplot params so the subplot(s) fits in to the figure area
plt.tight_layout()

# Saving the figure to the specified path before clearing the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/72.png', format='png')

# Clear the current figure after saving
plt.clf()
