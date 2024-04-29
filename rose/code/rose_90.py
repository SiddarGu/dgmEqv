
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels 
data_labels = ['Education', 'Healthcare', 'Infrastructure', 'Environment', 'Social Security', 'Immigration', 'Defense', 'Taxation']
data = [34, 80, 50, 30, 20, 15, 10, 5] 
line_labels = ['Policy Area', 'Number of Initiatives'] 

# Plot the data with the type of rose chart 
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='polar')

# Set up the axes in polar coordinates 
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# Set the number of ticks
num_categories = len(data_labels) 
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Calculate the sector angle
sector_angle = (2 * np.pi) / num_categories 

# Draw sectors corresponding to different categories 
colors = ['green', 'red', 'orange', 'purple', 'yellow', 'black', 'blue', 'brown'] 

for i in range(num_categories):
    ax.bar(i*sector_angle, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

# Reposition the legend so that it does not cover any part of the chart
ax.legend(bbox_to_anchor=(1.04, 0.5), loc="center left")

# Set each category label at the center of its corresponding sector
ax.set_xticklabels(data_labels)

# Set title for the figure
plt.title('Number of Government Policy Initiatives in 2021')

# Automatically resize the image 
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_75.png')

# Clear the current image state
plt.clf()