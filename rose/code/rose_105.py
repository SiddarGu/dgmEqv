
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Primary Care', 'Mental Health', 'Cardiology', 'Oncology', 'Ophthalmology', 'Endocrinology', 'Pediatrics', 'Geriatrics', 'Emergency Medicine']
data = [73, 63, 50, 42, 33, 27, 19, 12, 8]
line_labels = ['Category', 'Number of Hospitals']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

colors = ['#ff0000', '#0000ff', '#00ff00', '#ff00ff', '#008000', '#00FFFF', '#800080', '#FFFF00', '#FFA500']
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=14, color='k')

ax.legend(bbox_to_anchor=(1.2, 0.9))
plt.title("Number of Hospitals Specializing in Different Fields in 2021")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-054203_11.png')
plt.close(fig)