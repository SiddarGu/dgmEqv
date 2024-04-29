
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data = np.array([100, 60, 50, 30, 90, 20, 80, 40, 70])
data_labels = ["Beach Resorts","Mountains","Theme Parks","National Parks","Shopping Centers","Historic Sites","Museums","Amusement Parks","Restaurants"]
line_labels = ["Travel Destination","Number of Visits"]

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

# Calculate the sector angle 
sector_angle = (2 * np.pi) / len(data_labels)

# Create the sectors for different categories
for i, v in enumerate(data):
    ax.bar(sector_angle*i, v, width=sector_angle, label=data_labels[i])

# Assign a label to each sector when you create them
ax.legend(bbox_to_anchor=(1,0.5))

# Set the number of ticks
ax.set_xticks(sector_angle * np.arange(len(data_labels)))

# Set the labels for each tick
ax.set_xticklabels(data_labels, rotation=45, wrap=True)

# Set the title of the figure
ax.set_title("Number of Visits to Popular Tourist Attractions in 2021")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_30.png')

# Clear the current image state
plt.clf()