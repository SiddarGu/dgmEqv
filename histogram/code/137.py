import matplotlib.pyplot as plt
import numpy as np

# Data preparation
data_labels = ['Average Shipment Weight (Tons)', 'Number of Shipments']

line_labels = [
    '0-1', '1-2', '2-3', '3-4', '4-5',
    '5-6', '6-7', '7-8', '8-9', '9-10'
]

data = [
    320, 415, 275, 160, 95,
    80, 45, 25, 15, 10
]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Plotting histogram
ax.bar(line_labels, data, color=plt.cm.Paired(np.arange(len(data))))

# Adding grid
ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.5)

# Rotate x-axis labels if necessary
ax.set_xticklabels(line_labels, rotation=45, ha='right')

# Add title
ax.set_title('Volume of Shipments by Average Weight in Transportation Sector')

# Set axis labels
ax.set_xlabel(data_labels[0], wrap=True)
ax.set_ylabel(data_labels[1])

# Enable the tight layout to make sure everything fits without overlap
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/137.png'
plt.savefig(save_path, format='png')

# Clear current figure state
plt.clf()
