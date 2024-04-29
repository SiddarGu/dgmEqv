
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Performing Arts', 'Visual Arts', 'Literary Arts', 'Culinary Arts', 'Music', 'Architecture', 'Film', 'Design', 'Photography']
data = [100, 90, 80, 70, 60, 50, 40, 30, 20]
line_labels = ['Category', 'Number']

sector_angle = (2 * np.pi) / len(data_labels)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, bottom=0.0, label=data_labels[i], color=plt.cm.Set1(i))

ax.set_title("Number of Arts and Culture Events in 2021", fontsize=20)
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=15)
ax.set_yticklabels([])
ax.legend(loc="upper right", bbox_to_anchor=(1.1, 1.0))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_69.png')
plt.clf()