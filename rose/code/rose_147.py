
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Primary Education', 'Secondary Education', 'Undergraduate', 'Graduate', 'Post-Graduate', 'Doctoral']
data = [450, 750, 1350, 650, 250, 100]
line_labels = ['Level', 'Number of Students']

# Set up the figure
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1,1,1, projection='polar')

# Set the number of categories
num_categories = len(data_labels)

# Calculate the sector angle
sector_angle = (2 * np.pi) / num_categories

# Plot the data
for i in range(num_categories):
    ax.bar(x=sector_angle*i, height=data[i], width=sector_angle, bottom=0.0, color=plt.cm.jet(i/num_categories), label=data_labels[i])

# Set the xticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Set the xticklabels
ax.set_xticklabels(data_labels, fontsize=12)

# Set the legend
ax.legend(bbox_to_anchor=(1, 1), loc='upper left', fontsize=12)

# Set the title
plt.title("Number of Students at Different Education Levels in 2021")

# Resize the figure
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_28.png')

# Clear the current image state
plt.clf()