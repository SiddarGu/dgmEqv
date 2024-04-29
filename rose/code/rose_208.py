
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Physics', 'Chemistry', 'Engineering', 'Mathematics', 'Computer Science', 'Aerospace', 'Robotics', 'Biotechnology']
data = [50, 30, 20, 10, 50, 40, 20, 30]
line_labels = ['Category', 'Number of People']

# plot the data with the type of rose chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# modify the axes to use polar coordinates
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# set the number of ticks and labels
num_categories = len(data_labels)
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# set the color of each sector
colors = plt.cm.rainbow(np.linspace(0, 1, num_categories))

# calculate the sector angle
sector_angle = (2 * np.pi) / num_categories

# plot data line with different colors
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

# add legend
ax.legend(data_labels, bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='x-large')

# set title
plt.title('Number of Professionals in Scientific and Engineering Fields', fontsize=14)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_14.png')

# clear the current image state
plt.clf()