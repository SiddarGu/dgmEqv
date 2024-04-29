
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Automation', 'Robotics', 'Machinery', 'Tooling', 'Electronics', 'Casting', 'Sheetmetal', 'Plastics', 'Fabrication', 'Packaging']
data = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
line_labels = ['Category', 'Number']

# Create figure and plotting
fig = plt.figure(figsize=(14,14))
ax = fig.add_subplot(111, polar=True)

# Assign a different color to each sector and add a legend
cmap = plt.get_cmap('hsv')
colors = cmap(np.linspace(0, 1.0, len(data_labels)))
sector_angles = np.linspace(0, 2*np.pi, len(data_labels), endpoint=False)

for i, (data_label, color) in enumerate(zip(data_labels, colors)):
    ax.bar(sector_angles[i], data[i], width=sector_angles[1], bottom=0.0, label=data_label, color=color)

# Position the legend
ax.legend(bbox_to_anchor=(0.5, 1.1), 
          loc='upper center', 
          ncol=4, 
          frameon=True, 
          fontsize=12)

# Set the number of ticks to match the number of categories
ax.set_xticks(sector_angles)
ax.set_xticklabels(data_labels, fontsize=12)

# Set the title
ax.set_title('Production Capacity in the Manufacturing Industry', fontsize=16)

# Resize the image
plt.tight_layout()

# Save the plot
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_52.png', bbox_inches='tight')

# Clear the current image state
plt.clf()