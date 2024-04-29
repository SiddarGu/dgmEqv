
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Visual Arts','Performing Arts','Music','Literature','Architecture','Cinema','Fashion','Design']
data = [70,50,30,20,80,60,40,20]
line_labels = ['Category','Number']

# Create figure
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111, projection='polar')

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the data
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

# Set the x-axis ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))

# Set the x-axis labels
ax.set_xticklabels(data_labels, fontsize=12)

# Set legend
ax.legend(bbox_to_anchor=(1.1, 1.05))

# Set title
ax.set_title("Popularity of Arts and Culture Categories in 2021", fontsize=18)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_64.png')

# Clear the current image state
plt.clf()