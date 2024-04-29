
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Education', 'Healthcare', 'Environment', 'Community Development', 'Animal Welfare', 'Arts and Culture', 'Social Services']
data = [7000, 6000, 5000, 4000, 3000, 2000, 1000]
line_labels = ['Program Category', 'Number of Donors']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, polar=True)

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))

ax.set_theta_direction(-1)
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10)
ax.legend(bbox_to_anchor=(1.1, 0.8), fontsize=15, title=line_labels[0])

ax.set_title('Number of Donors Supporting Nonprofit Programs in 2021', fontsize=20)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_16.png')
plt.clf()