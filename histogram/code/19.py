import matplotlib.pyplot as plt
import numpy as np

# Given data
data_labels = ['<1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10']
line_labels = ['Quantity of Items']
data = np.array([500000, 450000, 400000, 350000, 300000, 250000, 200000, 150000, 100000, 50000])

# Create figure and add a subplot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(1, 1, 1)

# Create the histogram using the data
ax.bar(data_labels, data, color=plt.cm.viridis(np.linspace(0, 1, len(data_labels))))

# Setting grid, title, and labels
ax.set_title('Product Defects Rate Across Manufacturing Lines', fontsize=16)
ax.set_xlabel('Product Defects Rate (%)', fontsize=14)
ax.set_ylabel('Quantity of Items', fontsize=14)
ax.grid(axis='y', linestyle='--', linewidth=0.5)

# If the text length of the label is too long, rotate the labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", wrap=True)

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/19.png')

# Clear the current image state
plt.clf()
