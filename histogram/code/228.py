import matplotlib.pyplot as plt
import numpy as np
import os

# Provided data
data_labels = ['CO2 Emissions (Million Metric Tons)']
line_labels = ['United States', 'China', 'India', 'Russia', 'Japan', 'Germany', 'United Kingdom', 'France', 'Brazil', 'Canada']
data = [5000, 10300, 2400, 1600, 1200, 780, 415, 365, 260, 550]

# Create figure with larger figsize to prevent content from being cut off
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111)

# Create the vertical bar chart
bar_positions = np.arange(len(line_labels))
ax.bar(bar_positions, data, color='skyblue', edgecolor='black')

# Set the title of the figure
ax.set_title('National CO2 Emissions Overview: Environment and Sustainability', fontsize=14)

# Set labels for X and Y axes
ax.set_xlabel('Country', fontsize=12)
ax.set_ylabel(data_labels[0], fontsize=12)

# Set the position and labels of the X ticks
ax.set_xticks(bar_positions)
ax.set_xticklabels(line_labels, rotation=45, ha="right", fontsize=10, wrap=True)

# Add background grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust the layout
plt.tight_layout()

# Save the figure to the specified file path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/228.png'
# Ensure the directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure's state after saving to prevent reusing the same state
plt.clf()
