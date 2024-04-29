
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ['Research Grants (Millions of Dollars)', 'Patent Applications (Number)', 'Research Papers Published (Number)']
line_labels = ['Structural Engineering', 'Environmental Engineering', 'Electrical Engineering', 'Civil Engineering', 'Mechanical Engineering', 'Aerospace Engineering', 'Biomedical Engineering', 'Computer Science']
data = np.array([[290, 1450, 719], [420, 2900, 1250], [560, 3200, 1890], [580, 2300, 1090], [720, 1500, 795], [960, 1900, 899], [1360, 1900, 1450], [1380, 3500, 2190]])

plt.figure(figsize=(15, 10))

ax = plt.subplot(111)
ax.bar(line_labels, data[:, 0], width=0.3, color='green', alpha=0.6)
ax.set_xticks(np.arange(len(line_labels)))
ax.set_xticklabels(line_labels, rotation=45)
ax.set_ylabel(data_labels[0], color='green')
ax.tick_params(axis='y', colors='green')

ax2 = ax.twinx()
ax2.plot(line_labels, data[:, 1], linestyle='dashed', marker='o', color='blue')
ax2.set_ylabel(data_labels[1], color='blue')
ax2.tick_params(axis='y', colors='blue')

ax3 = ax.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.plot(line_labels, data[:, 2], linestyle='dashed', marker='*', color='red')
ax3.set_ylabel(data_labels[2], color='red')
ax3.tick_params(axis='y', colors='red')

plt.title('Science and Engineering Investment and Output Analysis')
ax.legend(data_labels, loc='upper left')
ax2.legend(data_labels, loc='upper center')
ax3.legend(data_labels, loc='upper right')
plt.grid(True)
plt.autoscale()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/7_2023122261325.png', bbox_inches='tight')
plt.clf()