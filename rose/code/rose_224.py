
import matplotlib.pyplot as plt
import numpy as np

# transform the data into three variables: data_labels, data, line_labels
data_labels = ['Adventure Tourism', 'Business Tourism', 'Cultural Tourism', 'Eco-Tourism', 'Educational Tourism', 'Heritage Tourism', 'Medical Tourism', 'Religious Tourism']
data = [170, 150, 130, 100, 80, 60, 40, 20]
line_labels = ['Type of Tourism', 'Number of Visitors']

# create figure
fig = plt.figure(figsize=(8, 8))

# plot the data with the type of rose chart
ax = fig.add_subplot(111, projection='polar', polar=True)

# assign a different color to each sector
colors = ['r', 'g', 'b', 'y', 'm', 'c', '#FFA500', '#808080']
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle
for i, color in enumerate(colors):
    ax.bar(i*sector_angle, data[i], width=sector_angle, bottom=0.0, color=color, alpha=0.5, label=data_labels[i])

# reposition the legend so that it does not cover any part of the chart
ax.legend(bbox_to_anchor=(1.5, 1), loc='upper right')

# set the number of ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))

# set category labels
ax.set_xticklabels(data_labels)

# draw background grids
ax.grid(True)

# set the title
plt.title('Number of Visitors to Different Types of Tourism in 2021')

# use tight_layout() to automatically resize the image
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_44.png')

# clear the current image state
plt.clf()