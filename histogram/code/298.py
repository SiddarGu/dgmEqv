import matplotlib.pyplot as plt
import numpy as np

# Data setup
data_labels = ['Percentage of Total Energy Production (%)']
line_labels = ['Solar Power', 'Wind Power', 'Hydroelectric', 'Biomass', 'Geothermal']
data = np.array([25.5, 20.2, 30.1, 15.3, 8.9])

# Create a figure and a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.barh(line_labels, data, color=plt.cm.rainbow(np.linspace(0, 1, len(data))))

# Adding the data labels above the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width - 1  # shift the text to the left side of the right end
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}%', va='center')

# Set the chart title
ax.set_title('Proportion of Renewable Energy Sources in Total Energy Production', fontsize=14)

# Show grid
ax.grid(axis='x', linestyle='--', alpha=0.7)

# If text length of label is too long, rotate or wrap labels
plt.yticks(wrap=True)

# Automatically resize the image
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/648.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure state
plt.clf()
