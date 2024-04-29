
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: 
data_labels = ['Hydroelectric', 'Solar', 'Wind', 'Geothermal', 'Nuclear', 'Biomass', 'Natural Gas']
data = [43, 97, 17, 36, 96, 60, 68]
line_labels = ['Type', 'Number']

# Create figure before plotting, i.e., add_subplot() follows plt.figure()
plt.figure(figsize=(10,10))
ax = plt.subplot(111, projection='polar')

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the data with the type of rose chart
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# Add legend
ax.legend(data_labels, bbox_to_anchor=(1.0, 1.0))

# Set the number of ticks 
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Set the labels 
ax.set_xticklabels(data_labels, fontsize=15, rotation=45, wrap=True)

# Set the title 
ax.set_title('Energy Sources Used by Utilities in 2021', fontsize=20)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_23.png')

# Clear the current image state
plt.clf()