
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Music', 'Visual Arts', 'Theater', 'Dance', 'Literature', 'Film', 'Photography', 'Poetry', 'Architecture']
data = [60, 75, 45, 30, 40, 50, 25, 20, 10]
line_labels = ['Category', 'Number']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

num_categories = len(data_labels)

sector_angle = (2 * np.pi) / num_categories

for i, data_val in enumerate(data):
    ax.bar(i * sector_angle, data_val, width=sector_angle, bottom=0.0, label=data_labels[i], color=plt.cm.Set1(i))

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12)

ax.legend(data_labels, bbox_to_anchor=(1, 1.2), fontsize=12)

ax.set_title("Popularity of Art Forms in 2021", fontsize=16)

plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-054203_8.png")
plt.clf()