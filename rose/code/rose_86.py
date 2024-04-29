
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Criminal Law', 'Civil Rights', 'Corporate Law', 'Family Law', 'Labor Law', 'Intellectual Property', 'Environmental Law', 'Tax Law', 'International Law']
data = [100, 85, 75, 60, 50, 45, 40, 35, 30]
line_labels = ['Legal Practice Area', 'Number of Attorneys']

fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

colors = [plt.cm.jet(i/ num_categories) for i in range(num_categories)]

for i in range(num_categories):
    ax.bar(sector_angle*i, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

ax.set_xticks(sector_angle/2 + sector_angle * np.arange(num_categories))
ax.set_xticklabels(data_labels, fontsize=14)

ax.legend(data_labels, bbox_to_anchor=(1.2, 0.2))
ax.set_title('Number of Attorneys Practicing in Different Legal Areas in 2021', fontsize=16)

fig.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_71.png')
plt.clf()