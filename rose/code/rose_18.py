
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
# Data_labels represents the labels of each column except the first column. 
# Line_labels represents the labels of each row except the first row. 
# Data represent the numerical array in the data.
data_labels = ['Artificial Intelligence', 'Cloud Computing', 'Cybersecurity', 
               'Big Data', 'Internet of Things', 'Robotics', 'Augmented Reality']
data = [25, 45, 30, 50, 20, 35, 10]
line_labels = ['Technology', 'Number']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Create figure before plotting, i.e., add_subplot() follows plt.figure()
ax.set_theta_direction(-1)
ax.set_title('Number of Companies Utilizing Different Technologies in 2021')

# Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'.
# This change will set up the axes in polar coordinates, which is necessary for creating a rose chart. 
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Different sectors represent different categories with the same angle, 
# whose radius is proportional to the corresponding value, 
# and the angles of these sectors must add up to 360 degrees
# Assign a different color to each sector
colors = ['crimson', 'darkorange', 'forestgreen', 
          'royalblue', 'indigo', 'violet', 'pink']
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], 
           width=sector_angle, 
           label=data_labels[i], 
           color=colors[i])

# Add a legend next to the chart that clearly labels 
# the category each sector represents
ax.legend(data_labels, bbox_to_anchor=(1.25, 0.6))

# Ensure that the number of ticks set with `ax.set_xticks()` 
# matches exactly the number of categories or labels you have in `data_labels`.  
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, 
                          endpoint=False))

# Make sure that each category label is correctly positioned
# at the center of its corresponding sector
ax.set_xticklabels(data_labels, fontsize=12, wrap=True,
                   rotation=45)

# Drawing techniques such as background grids can be used
ax.grid(linestyle='dotted')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_3.png')

# Clear the current image state at the end of the code
plt.clf()