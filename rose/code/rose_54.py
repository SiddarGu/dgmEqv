
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Cloud Computing','Artificial Intelligence','Big Data','Cybersecurity','Internet of Things','Virtual Reality','Blockchain']
data = [50,40,30,20,10,5,4]
line_labels = ['Category', 'Number']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(sector_angle*i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i/num_categories))

# Add legend
ax.legend(data_labels, bbox_to_anchor=(0.6, 0.2, 0.2, 0))

# Set ticks and labels
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, ha='left')

# Set title
ax.set_title('Number of Companies Utilizing New Technologies in 2021')

# Adjust the layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_149.png')

# Clear the current image state
plt.clf()