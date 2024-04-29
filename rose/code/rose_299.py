
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Road', 'Rail', 'Air', 'Maritime', 'Pipeline', 'Courier']
data = [150, 120, 80, 60, 40, 20]
line_labels = ['Mode of Transport', 'Number of Users']

num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.set_title('Number of People Utilizing Different Modes of Transport for Logistics in 2021', pad=20)

# plot the sectors
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# set the starting points of the sectors
ax.set_theta_offset(np.pi / 2)

# set the direction in which the sectors appear
ax.set_theta_direction(-1)

# set the number of ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))

# set the labels of the ticks
ax.set_xticklabels(data_labels, wrap=True, fontsize=10)

# draw the legend
ax.legend(bbox_to_anchor=(1.1, 1.1))

# save the plot
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/4.png')

# clear the current image state
plt.clf()