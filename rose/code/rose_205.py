
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Math","Science","English","Social Studies","Technology","Arts","Physical Education","Foreign Language","Music"]
data = [200, 170, 180, 160, 150, 140, 100, 80, 60]
line_labels = []

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    line_labels.append(data_labels[i])
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(line_labels, fontsize=12, va="center")
ax.legend(bbox_to_anchor=(1.1, 1), fontsize=12)
ax.set_title("Number of Students Enrolled in Different Academic Areas in 2021", fontsize=14)
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_54.png")
plt.clf()