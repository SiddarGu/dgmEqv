
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Full-time Employees', 'Part-time Employees', 'Contract Employees', 'Temporary Employees', 'Interns']

data = [80, 40, 20, 10, 5]

line_labels = ['Employee Type', 'Number']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

num_categories = len(data)

sector_angle = (2 * np.pi) / num_categories

angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

ax.set_xticks(angles)
ax.set_xticklabels(data_labels, fontsize=14)

for i in range(num_categories):
    ax.bar(angles[i], data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Dark2(i))

ax.legend(bbox_to_anchor=(1, 1))

ax.set_title('Number of Employees by Type in 2020', fontsize=16)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_48.png')
plt.clf()