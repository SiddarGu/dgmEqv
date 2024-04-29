
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Physics","Chemistry","Mathematics","Computer Science","Electrical Engineering","Mechanical Engineering","Aerospace Engineering","Civil Engineering"]
data = [50,40,30,25,20,15,10,5]
line_labels = ["Field","Number of Scientists"]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(len(data)):
    ax.bar(i*sector_angle, data[i], width=sector_angle, bottom=0.0, label=data_labels[i], color=f"C{i}")

ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10)
ax.set_title('Number of Scientists in Each Field of Science and Engineering in 2021', fontsize=15)

ax.legend(bbox_to_anchor=(1.1, 0.5), fontsize=10)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_2.png')
plt.clf()