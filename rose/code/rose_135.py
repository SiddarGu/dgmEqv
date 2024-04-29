
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Artificial Intelligence', 'Machine Learning', 'Blockchain', 'Cyber Security',
               'Cloud Computing', 'Data Science', 'Networking', 'Robotics', 'IoT']
data = [40, 50, 30, 60, 70, 80, 90, 100, 20]
line_labels = ['Category', 'Number']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'violet', 'brown']

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=90)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
ax.set_title('Popularity of Technology and Internet Fields in 2021')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_145.png')
plt.clf()