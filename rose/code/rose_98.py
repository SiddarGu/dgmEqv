
import matplotlib.pyplot as plt 
import numpy as np 

# Transform the given data into three variables 
data_labels = ["Fast Food", "Chinese Cuisine", "Italian Cuisine", "Japanese Cuisine", "French Cuisine", "American Cuisine", "Mexican Cuisine", "Indian Cuisine", "Seafood"]
line_labels = ["Number"]
data = np.array([[110, 120, 100, 90, 80, 70, 60, 50, 40]])

# Create figure before plotting 
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='polar')

# Plot the data with the type of rose chart
sector_angle = (2 * np.pi) / len(data_labels)

# Create sectors corresponding to different categories
for i, value in enumerate(data[0]):
    ax.bar(i * sector_angle, value, width=sector_angle, label=data_labels[i])

# Add legend to chart 
ax.legend(data_labels, bbox_to_anchor=(1.5, 0.75), loc="center")

# Set ticks on chart 
ax.set_xticks([sector_angle * i for i in range(len(data_labels))])
ax.set_xticklabels(data_labels, rotation=90)

# Set title
ax.set_title("Popularity of Various Cuisines in the Food and Beverage Industry", fontsize=16)

# Tight layout and save the figure 
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_9.png')

# Clear the current image state
plt.clf()