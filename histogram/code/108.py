import matplotlib.pyplot as plt
import numpy as np

# Data
data_labels = ['Social Networking', 'Online Shopping', 'News Websites', 'Video Streaming', 
               'Online Gaming', 'Email Communication', 'Forums and Communities']
data = [2.5, 1.8, 1.2, 3.1, 2.2, 0.9, 1.3]

# Create figure and add subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Vertical Bar/Histogram Plot
ax.bar(data_labels, data, color=plt.cm.Paired(np.arange(len(data_labels))))

# Add grid
ax.yaxis.grid(True)

# Set the title
ax.set_title('Daily Average Internet Usage Across Various Web Activities')

# Formatting the x-axis labels to be clear and non-overlapping
ax.set_xticklabels(data_labels, rotation=45, ha='right', wrap=True)

# Automatically adjust subplot params for the figure to fit into the display area
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1011.png'
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
