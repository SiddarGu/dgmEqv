
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Visual Arts", "Music", "Dance", "Literature", "Theater", "Film"]
data = np.array([50, 80, 60, 90, 40, 70])
line_labels = ["Category", "Number"]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, polar=True)
num_categories = len(data_labels)

sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])
    
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10)
ax.legend(bbox_to_anchor=(1, 0.5), loc='center left')

ax.set_title("Total Number of Arts and Culture Activities in 2021", fontsize=14)

fig.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_4.png")
plt.clf()