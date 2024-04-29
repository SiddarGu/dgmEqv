
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ['Solar', 'Wind', 'Hydro', 'Natural Gas', 'Nuclear', 'Biomass']
data = [95, 87, 63, 50, 30, 15]
line_labels = ['Energy Source', 'Number']

# Create the figure and set the axes to use polar coordinates
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='polar')

# Calculate the sector angle
sector_angle = (2 * np.pi) / len(data_labels)

# Plot the sectors corresponding to different categories
for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i/len(data_labels)))

# Create and reposition the legend
ax.legend(bbox_to_anchor=(1, 0.5), loc="center left")

# Set the number of ticks to match the number of labels
ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False))

# Set the labels for each tick
ax.set_xticklabels(data_labels)

# Set the title of the figure
plt.title("Energy Generation by Source in 2021")

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_77.png')

# Clear the current image state
plt.clf()