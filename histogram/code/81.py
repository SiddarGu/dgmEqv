import matplotlib.pyplot as plt
import numpy as np

# Data provided
data = np.array(
    [75, 64, 78, 82, 89, 95, 88, 77, 79, 90, 110, 130]   # Number of Stores (duplicated for example)
)

data_labels = ["Number of Stores"]
line_labels = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Set up the figure size and add subplots
fig, ax = plt.subplots(figsize=(14, 7))

# Plot the histograms
ax.bar(np.arange(len(line_labels)), data, label=data_labels[0], width=0.35)

# Set the title
ax.set_title('Monthly Retail E-commerce Sales Trends')

# Formatting the X-axis
ax.set_xticks(np.arange(len(line_labels)) + 0.35 / 2)
ax.set_xticklabels(line_labels, rotation=45, ha="right")

# Enable the grid, label the axes
ax.grid(True)
ax.set_axisbelow(True)
ax.set_xlabel('Month')
ax.set_ylabel('Value')

# Add a legend
ax.legend()

# Resize the image with tight_layout and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/histogram/png/81.png')

# Clear the current image state after saving the plot
plt.clf()
