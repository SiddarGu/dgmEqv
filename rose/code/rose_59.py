
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Accounting','Investment','Banking','Marketing','Economics','Real Estate','Insurance','Taxation']
data = [45,100,85,73,50,42,32,20]
line_labels = ['Business Category','Number']

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label = data_labels[i])

ax.legend(bbox_to_anchor=(1.05, 0.55), labels=data_labels)
ax.set_title('Number of Businesses Operating in Each Field in 2021')
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_20.png')
plt.clf()