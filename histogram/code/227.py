import matplotlib.pyplot as plt
import numpy as np
import os

# Data
data_labels = ['Browser Market Share (%)']
line_labels = ['Chrome', 'Safari', 'Edge', 'Firefox', 'Opera', 'Others']
data = [63.2, 19.6, 7.5, 5.2, 2.1, 2.4]

# Create figure and axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot histogram
bars = ax.bar(line_labels, data, color=plt.cm.tab10(np.arange(len(data))), edgecolor='black')

# Set title
ax.set_title('Browser Usage Distribution Across the Web')

# Set grid
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)
ax.set_ylabel(data_labels[0])
# Set rotation for long labels
plt.xticks(rotation=45, ha='right')

# Make sure all characters are shown and not overwritten
plt.tight_layout()

# Saving path
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/histogram/png_val/227.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig(save_path)

# Clear the current image state
plt.clf()
