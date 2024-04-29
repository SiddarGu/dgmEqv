
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['STEM', 'Liberal Arts', 'Education', 'Social Sciences', 'Arts and Humanities', 'Agriculture', 'Business'] 
data = [750, 400, 350, 200, 150, 100, 50]
line_labels = ['Category', 'Number']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(polar=True)

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))

ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi / 2)

ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels)

ax.legend(bbox_to_anchor=(1.3,1), loc="upper right")
ax.set_title("Number of Students Enrolled in Different Academic Fields in 2021")

fig.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_27.png')

plt.clf()