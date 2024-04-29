
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Grocery', 'Department Stores', 'Clothing Stores', 'Electronics', 'Home Improvement', 'Pharmacies', 'Bookstores', 'Specialty Stores']
data = [30, 40, 50, 60, 70, 80, 90, 100]
line_labels = ['Category', 'Number']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi/2)

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

ax.legend(bbox_to_anchor=(1.13, 1.05))
ax.set_title('Number of Stores by Retail Category in 2021')
ax.set_xticks(sector_angle * np.arange(num_categories))
ax.set_xticklabels(data_labels, fontsize=10, rotation=60, wrap=True)
plt.tight_layout()

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_75.png')
plt.clf()