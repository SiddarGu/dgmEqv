
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ["Nuclear","Solar","Wind","Hydroelectric","Geothermal","Biomass","Natural Gas"]
line_labels = ["Energy Source","Number of Plants"]
data = [[68,50,43,25,15,10,5]]

# Plot the data with the type of rose chart. 
fig = plt.figure()
ax = fig.add_subplot(polar=True)
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create sectors for each category with the same angle, whose radius is proportional to the corresponding value.
for i in range(num_categories):
    ax.bar(sector_angle * i, data[0][i], width=sector_angle, label=data_labels[i])

# Set the ticks and labels.
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Reposition the legend so that it does not cover any part of the chart.
ax.legend(bbox_to_anchor=(1.2, 0.9))

# Set the title of the figure.
ax.set_title("Number of Power Plants by Energy Source in 2021")

# Automatically resize the image by tight_layout().
plt.tight_layout()

# Save the image.
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_110.png")

# Clear the current image state.
plt.clf()