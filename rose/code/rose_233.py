
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Networking", "Operating Systems", "Programming", "Database", "Security", "Virtualization", "Cloud Computing", "Artificial Intelligence"]
data = [75, 60, 50, 40, 30, 20, 10, 5]
line_labels = ["Category", "Number"]

fig = plt.figure(figsize=(10,10))

ax = fig.add_subplot(111, projection='polar')
ax.set_title('Number of Companies Adopting Technologies in 2021')

sector_angle = (2 * np.pi) / len(data_labels)

for i in range(len(data_labels)):
    ax.bar([sector_angle * i], [data[i]], width=sector_angle, label=data_labels[i], color=plt.cm.jet(i/len(data_labels)))

ax.legend(bbox_to_anchor=(1.1, 1.05))
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, rotation=90)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_7.png')
plt.show()
plt.clf()