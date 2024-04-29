
import matplotlib.pyplot as plt
import numpy as np

data = [[90,75,50,30,20,10]]
data_labels = ['Single Family Home', 'Condominium', 'Apartment Complex', 'Townhouse', 'Vacation Home', 'Mobile Home']
line_labels = ['Number of Properties']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

for i in range(num_categories):
    ax.bar(i * sector_angle, data[0][i], width=sector_angle, alpha=0.8, color=plt.cm.viridis(i/num_categories), label=data_labels[i])

ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')

# Set the position of the x ticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Set the labels of the x ticks
ax.set_xticklabels(data_labels, fontsize=12)

# Add legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)

# Add title
plt.title('Number of Properties in Different Types in Real Estate and Housing Market', fontsize=14)

# Set the label of the y-axis
plt.ylabel('Number of Properties', fontsize=14)

# Set the label of the x-axis
plt.xlabel('Property Type', fontsize=14)

plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_144.png')

# Clear the current image state
plt.clf()