
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ["North America","South America","Europe","Africa","Asia","Australia","Antarctica"]
data = [450,250,800,300,700,100,50]
line_labels = ["Number of Tourists"]

# Plot the data with the type of rose chart.
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# Create sectors for each category
for i, value in enumerate(data):
    ax.bar(sector_angle * i, value, width=sector_angle, label=data_labels[i])

# Create legend and adjust its position
ax.legend(bbox_to_anchor=(1.2,1), loc='upper right', labels=data_labels)

# Set the number of ticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Set the labels of each tick
ax.set_xticklabels(data_labels, rotation=15)

# Set the title of the figure
plt.title("Number of Tourists Visiting Each Region in 2021")

# Resize the figure
plt.tight_layout()

#Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_19.png')

#Clear the current image state
plt.clf()