
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Social Media', 'Video Streaming', 'Messaging', 'Web Search', 'Shopping', 'Gaming', 'Financial Services', 'News', 'Maps']
line_labels = ['Topic', 'Number of Users']
data = np.array([[800, 400, 350, 300, 250, 200, 150, 100, 50]])

# Plot the data with the type of rose chart
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

# Set up the axes in polar coordinates, which is necessary for creating a rose chart
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# Calculate the sector angle and draw sectors corresponding to different categories 
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Assign a different color to each sector and create a legend to label the category each sector represents
colors = plt.cm.jet(np.linspace(0, 1, num_categories))
for i in range(num_categories):
    ax.bar(i * sector_angle, data[0, i], width=sector_angle, color=colors[i], label=data_labels[i])
ax.legend(bbox_to_anchor=(1.2, 0.8))

# Set the number of ticks to match the number of categories or labels in data_labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False)) 

# Set each category label correctly positioned at the center of its corresponding sector
ax.set_xticklabels(data_labels, rotation=45, ha='right')

# Plot the background gridlines
ax.grid(True)

# Resize the image by tight_layout()
plt.tight_layout()

# Set the title of the figure
plt.title('Popularity of Web Services in 2021')

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_22.png')

# Clear the current image state
plt.clf()