
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Users (Millions)', 'Monthly Active Users (Millions)', 'Average Daily Use (Hours)']
line_labels = ['YouTube', 'Twitter', 'Instagram', 'Snapchat', 'WhatsApp', 'WeChat', 'Reddit', 'LinkedIn', 'Tumblr', 'Pinterest', 'Facebook']
data = np.array([[2.0, 1.8, 3.3], [330, 320, 2.4], [1.6, 1.4, 2.2], [0.8, 0.7, 1.9], [1.6, 1.5, 2.1], [1.2, 1.1, 1.8], [0.5, 0.4, 1.5], [0.6, 0.5, 1.1], [0.3, 0.2, 1.0], [0.4, 0.3, 0.9], [2.4, 2.3, 2.5]])

fig = plt.figure(figsize=(15,12))
plot_types = [plt.bar, plt.plot, plt.scatter, plt.fill_between]

ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], width=0.8, alpha=0.8, color='b')
ax1.set_ylabel(data_labels[0], color='b', fontsize=14)
ax1.set_xlabel('Category', fontsize=14)
ax1.tick_params(axis='x', labelrotation=90)
ax1.set_title('Social Media and the Web: User Statistics and Trends', fontsize=20)

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'rs-', linewidth=3)
ax2.set_ylabel(data_labels[1], color='r', fontsize=14)

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.plot(line_labels, data[:,2], 'g^-', linewidth=3)
ax3.set_ylabel(data_labels[2], color='g', fontsize=14)

ax1.legend(['Users (Millions)'], loc='upper left')
ax2.legend(['Monthly Active Users (Millions)'], loc='upper center')
ax3.legend(['Average Daily Use (Hours)'], loc='upper right')

plt.grid(axis='y', linestyle='--')
ax1.xaxis.set_ticks(np.arange(len(line_labels)))
ax1.xaxis.set_ticklabels(line_labels)
ax2.xaxis.set_ticks(np.arange(len(line_labels)))
ax3.xaxis.set_ticks(np.arange(len(line_labels)))
ax2.autoscale()
ax3.autoscale()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/8_2023122270030.png')
plt.clf()