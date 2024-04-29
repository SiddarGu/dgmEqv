
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Waste Management', 'Renewable Energy', 'Sustainable Agriculture', 'Climate Change', 'Environmental Conservation', 'Pollution Control']
data = [50, 40, 30, 20, 10, 5] 
line_labels = ['Waste Management', 'Renewable Energy', 'Sustainable Agriculture', 'Climate Change', 'Environmental Conservation', 'Pollution Control']

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 8))

# Plot data with polar coordinates
ax = plt.subplot(111, projection='polar')

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories 

# Plot data and set labels
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=line_labels[i])

# Set legend
ax.legend(data_labels, bbox_to_anchor=(1.2, 1), fontsize='large')

# Set ticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories + 1)[:-1])
ax.set_xticklabels(data_labels, fontsize='large', rotation=45, ha='right', wrap=True)

# Set title
plt.title('Environmental Sustainability in the 21st Century', fontsize='x-large')

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_95.png')

# Clear current image state
plt.clf()