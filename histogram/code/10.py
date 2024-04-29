import matplotlib.pyplot as plt
import numpy as np

# Data from the question
data = [
    [2760, 'Facebook'],
    [2291, 'YouTube'],
    [2000, 'WhatsApp'],
    [1500, 'Instagram'],
    [1209, 'WeChat'],
    [1000, 'TikTok'],
    [514, 'Snapchat'],
    [396, 'Twitter'],
    [430, 'Reddit'],
    [322, 'Pinterest']
]

# Transpose the data to get data_labels and line_labels
data_labels = ['Active Users (Millions)']
line_labels = [row[1] for row in data]
data_values = [row[0] for row in data]

# Create the figure and the single subplot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the vertical histogram
ax.bar(line_labels, data_values, color=plt.cm.tab10(np.linspace(0, 1, len(data_values))))

# Set the title of the figure
ax.set_title('Active User Count of Top Social Media Platforms')

# Set x-axis label
ax.set_xlabel('Social Network')

# Set y-axis label
ax.set_ylabel('Active Users (Millions)')

# Add grid to the background
ax.yaxis.grid(True)

# Rotate x-axis labels if too long
plt.xticks(rotation=45, ha='right')

# Automatically adjust subplot params for the plot to fit into the figure area
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/10.png'
plt.savefig(save_path, format='png')

# Clear the current figure state after saving the plot
plt.clf()

