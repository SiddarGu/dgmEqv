
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Social Networking', 'Online Shopping', 'Video Streaming', 'Search Engines', 'E-mail', 'Online Advertising', 'Online Communities', 'Online Banking']
data = np.array([67, 88, 50, 69, 40, 30, 20, 10])
line_labels = ['Category', 'Number']

# set up the figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')
ax.set_theta_direction(-1)

# draw the rose chart
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for idx, label in enumerate(data_labels):
    ax.bar(sector_angle * idx, data[idx], width=sector_angle, label=label, color=plt.cm.Set1(idx/num_categories))

# set ticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=14, wrap=True, rotation=90)

# set title and legend
ax.set_title('Popularity of Online Services in 2021', fontsize=20)
ax.legend(bbox_to_anchor=(1.3, 0.9), fontsize=14)

# resize the image
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_12.png')

# Clear the current image state
plt.clf()