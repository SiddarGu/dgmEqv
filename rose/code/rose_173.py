
import matplotlib.pyplot as plt
import numpy as np

# Transform the data into three variables
data_labels = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Natural Gas', 'Coal', 'Nuclear', 'Oil']
data = np.array([90, 83, 76, 69, 62, 55, 48, 41])
line_labels = ['Type of Energy']

# Create figure and set axes
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the data as a rose chart
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, 
           label=data_labels[i], color=plt.cm.Set1(i/num_categories))

# Add legend
ax.legend(bbox_to_anchor=(1.3, 0.7), labels=data_labels, fontsize=10)

# Set tick labels
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Make sure the correct angle is used
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi/2)

# Add title
plt.title('Popularity of Energy Sources in 2021')

# Automatically adjust the position of the text
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_8.png')

# Clear the current image state
plt.clf()