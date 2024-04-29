
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Visual Arts','Dance','Music','Theatre','Literature','Film','Architecture','Crafts','Photography','Fashion']
data = [53,47,43,40,37,33,30,27,23,20]
line_labels = ['Category','Number']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(projection='polar')

# Set the number of categories
num_categories = len(data_labels)

# Calculate the sector_angle
sector_angle = (2 * np.pi) / num_categories

# Draw sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i])

# Position the legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Set the ticks and labels
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=20)

# Adjust the plot
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_title('Popularity of Arts and Culture Forms in 2021', fontsize=30)

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_13.png')
plt.clf()