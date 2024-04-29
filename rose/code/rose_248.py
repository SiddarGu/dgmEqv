

import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Math", "Science", "Language Arts", "Social Studies", "Physical Education", "Arts", "Music"]
data = [200, 170, 150, 125, 90, 70, 50]
line_labels = ["Category", "Number of Students"]

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, polar=True)

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

ax.legend(bbox_to_anchor=(1.1, 1), loc="upper left")

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, rotation=90)
ax.set_title('Enrollment of Students in Various Subjects in 2021')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_100.png')
plt.clf()