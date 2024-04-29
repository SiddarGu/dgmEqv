
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Physics','Mathematics','Engineering','Computer Science',
               'Chemistry','Biology','Aerospace Engineering','Environmental Science']
data = [120,80,200,150,100,50,40,30]
line_labels = ['Field of Study','Number of Students']

# Create figure before plotting
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='polar')

# Plot data with the type of rose chart
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], 
           width=sector_angle,
           label=data_labels[i],
           color=plt.cm.Spectral(i / num_categories))

# Add legend
ax.legend(data_labels, bbox_to_anchor=(1.15, 1.05))

# Set ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, fontweight='bold', horizontalalignment='center')

# Set title
ax.set_title('Number of Students Enrolled in Science and Engineering Fields in 2021', fontsize=15, fontweight='bold')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_22.png')

# Clear the current image state
plt.clf()