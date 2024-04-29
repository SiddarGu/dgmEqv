
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Renewable', 'Non-Renewable', 'Nuclear', 'Natural Gas', 'Solar', 'Wind', 'Hydroelectric']
data = [50, 90, 80, 60, 40, 20, 10]
line_labels = ['Type of Energy', 'Number of Sources']

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

colors = ['#ff0000', '#00f0ff', '#0000ff', '#ff00ff', '#00ff00', '#ff0080', '#ffff00']

for i,data_label in enumerate(data_labels):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=colors[i], label=data_label)

ax.legend(bbox_to_anchor=(1.15,1), loc="upper right")
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=15)
plt.title('Energy Generation Sources in 2021', fontsize=20)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_140.png')
plt.clf()