
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Revenue (Billions of Dollars)", "Average Time Spent (Hours)", "Users (Millions)"]
line_labels = ["Messaging Apps", "Video Sharing", "Blogging", "Social Networking", "E-Commerce", 
               "E-Learning", "Online Gaming", "Online Shopping", "Multimedia Sharing"]
data = np.array([[0.7, 4, 2.7], [2.3, 2, 3.1], [1.2, 3, 2.8], [6.2, 2.5, 4.8], [6.2, 1.5, 2.3], 
                 [1.2, 3, 1.3], [3.4, 2.5, 2.5], [4.3, 1.5, 2.8], [1.4, 2.5, 2.2]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:, 0], width=0.2, color='b', alpha=0.5, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
x_range = np.arange(len(line_labels))
ax1.set_xticks(x_range)
ax1.set_xticklabels(line_labels, rotation=30)
ax1.set_xlabel("Category")
ax1.tick_params(axis='y', colors='b')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], 'r-o', alpha=1, label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params(axis='y', colors='r')

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], 'g--', alpha=1, label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='g')
ax3.tick_params(axis='y', colors='g')
ax3.spines['right'].set_position(('axes', 1.1))
ax3.spines['right'].set_visible(True)

ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.3), fancybox=True, shadow=True, ncol=3)
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), fancybox=True, shadow=True, ncol=3)
ax3.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), fancybox=True, shadow=True, ncol=3)

ax1.grid(True)
ax1.set_title("Digital Market Performance: Social Media, Net-based Businesses, and Other Web Services")

ax1.autoscale()
ax2.autoscale()
ax3.autoscale()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/36_2023122261325.png')
plt.clf()