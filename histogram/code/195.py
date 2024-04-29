import matplotlib.pyplot as plt
import os
import numpy as np

# Given data
data_labels = ["0-200", "200-400", "400-600", "600-800", "800-1000", "1000-1200", "1200-1400", "1400-1600", "1600-1800"]
data = [3, 5, 7, 2, 2, 1, 0, 0, 1]
line_labels = ["Monthly Active Users (Million)"]  # Not used in histograms, but defined as per instructions

# Create a figure and add a subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot the horizontal histogram
ax.barh(data_labels, data, color=plt.cm.viridis(np.linspace(0, 1, len(data))))

# Set title and labels
ax.set_title('Active User Distribution Across Social Media Platforms')
ax.set_xlabel('Number of Platforms')

# Grid, legends and layout
ax.grid(True, which='both', axis='both', linestyle='--', linewidth=0.5)
ax.legend(['Number of Platforms'], loc='lower right')

# Adjust layout
plt.tight_layout()

# Create directories if not exists
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Save the figure
plt.savefig(f'{save_dir}/195.png')

# Clear the current figure state
plt.clf()
