
import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ['Air Pollution', 'Water Pollution', 'Waste Management', 'Biodiversity Loss', 'Climate Change', 'Overfishing', 'Deforestation', 'Soil Pollution', 'Desertification']
data = [50, 60, 80, 20, 90, 25, 30, 40, 10]
line_labels = ['Environmental Issue', 'Number of Incidents']

# Create figure
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='polar')

# Plot data
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], sector_angle, edgecolor='k', label=data_labels[i])

# Format chart
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=14, rotation=30)
ax.legend(bbox_to_anchor=(1.15, 1.00))
ax.set_title('Environmental Incidents in 2021', fontsize=18)

# Add gridlines and background
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.grid(True)

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_84.png')

# Clear current image state
plt.clf()