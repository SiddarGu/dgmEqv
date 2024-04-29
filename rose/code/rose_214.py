
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Cinema", "Music", "Theatre", "Video Games", "Sports", "Gambling", "Amusement Parks"]
data = [82, 64, 48, 36, 25, 16, 8]
line_labels = ["Category", "Number"]

# Plot the data with the type of rose chart.
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

# Create figure before plotting, i.e., add_subplot() follows plt.figure().
# Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'.
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories # Calculate the sector angle

# Different sectors represent different categories with the same angle, whose radius is proportional to the corresponding value
# and the angles of these sectors must add up to 360 degrees
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

# Use a loop to assign a label to each sector when you create them with `ax.bar`
ax.legend(bbox_to_anchor=(1.25, 1)) # Reposition the legend so that it does not cover any part of the chart

# Ensure that the number of ticks set with `ax.set_xticks()` matches exactly the number of categories or labels you have in `data_labels`. 
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Set each category label at the center of its corresponding sector
ax.set_xticklabels(data_labels, fontsize=15)

# Use background grids
ax.grid(color='k', linestyle='-', linewidth=1)

# Set the title of the figure
ax.set_title('Number of Visitors to Sports and Entertainment Venues in 2021', fontsize=20)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_22.png')
# Clear the current image state
plt.clf()