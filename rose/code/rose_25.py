
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Solar Power', 'Wind Power', 'Natural Gas', 'Nuclear Power', 'Hydroelectricity']
data = [50, 40, 30, 20, 10]
line_labels = ['Source', 'Number']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i, data_val in enumerate(data):
    ax.bar(sector_angle * i, data_val, width=sector_angle, label=data_labels[i])

ax.set_xticks(np.linspace(sector_angle / 2, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, wrap=True, fontsize=9)
ax.legend(bbox_to_anchor=(1.1, 0.9))
ax.set_title('Energy Production by Source in 2021', fontsize=14)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_105.png')
plt.clf()