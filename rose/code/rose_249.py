
import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ['Painting', 'Music', 'Dance', 'Theater', 'Literary Arts', 'Cinematography', 'Sculpture', 'Architecture', 'Photography']
data = [50, 80, 30, 90, 35, 60, 40, 25, 20]
line_labels = ['Category', 'Number']

# Initialize figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

# Calculate sector angles
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Set colors for each category
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pink', 'purple']

# Plot data
for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

# Set chart title
ax.set_title('Popularity of the Arts Across Different Categories in 2021', fontsize=16, pad=15)

# Set number of ticks to match number of categories
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Set tick labels to match categories
ax.set_xticklabels(data_labels, fontsize=14, ha='center', rotation=45, wrap=True)

# Add legend
ax.legend(data_labels, bbox_to_anchor=(1.2, 0.7))

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_12.png')

# Clear the current image state
plt.clf()