
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Burgers","Salads","Sandwiches","Pizza","Fries","Soft Drinks","Milkshakes","Ice Cream","Coffee","Tea"]
data = [120,90,80,70,60,50,40,30,20,10]
line_labels = ["Product","Number of Orders"]

# Plot the data with the type of rose chart
# Create figure before plotting
fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111,projection='polar')

# Modify the axes to use polar coordinates
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Draw sectors corresponding to different categories
# Assign a different color to each sector
for i, v in enumerate(data):
    ax.bar(i*sector_angle, v, width=sector_angle, 
           label=data_labels[i], color=plt.cm.jet(i/num_categories))

# Set the number of ticks matches the number of categories
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Set the label of ticks
ax.set_xticklabels(data_labels, fontsize=10, wrap=True, rotation=-90)

# Position the legend
ax.legend(bbox_to_anchor=(1,1), fontsize=10)

# Set the title of figure
ax.set_title('Most Popular Food and Beverage Items in 2021')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_1.png')

# Clear the current image state
plt.cla()