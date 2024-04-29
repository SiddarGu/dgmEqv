
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ['Road','Rail','Air','Sea','Pipeline','Multi-modal']
line_labels = ['Number of Shipments']
data = [[3000,2500,2000,1500,1000,500]]

fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111,projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(i*sector_angle, data[0][i], width=sector_angle, label=data_labels[i], facecolor=np.random.rand(3,))
ax.set_xticks(np.linspace(0,2*np.pi,num_categories,endpoint=False))
ax.set_xticklabels(data_labels, fontsize=16)
ax.legend(bbox_to_anchor=(1.2, 0.9), fontsize=16)
ax.set_title('Number of Shipments Using Different Transport Modes in 2020', fontsize=20)
plt.tight_layout()

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_85.png')
plt.clf()