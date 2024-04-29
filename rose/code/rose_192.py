
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Air","Rail","Road","Sea","Pipeline"]
data = [100,80,60,40,20]
line_labels = ["Mode of Transport","Number"]

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(1,1,1,projection='polar')

ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")

for i in range(num_categories):
    color = plt.cm.Set1(i/num_categories)
    ax.bar(sector_angle*i, data[i], width=sector_angle, edgecolor='black', align='edge', label=data_labels[i], color=color)

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=90, fontsize=20)
ax.legend(bbox_to_anchor=(1.02, 1.0), loc="upper left", fontsize=20)

plt.title("Volume of Transport by Mode in 2021", fontsize=20)
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_32.png")
plt.clf()