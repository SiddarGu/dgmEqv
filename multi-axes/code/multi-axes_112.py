import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

fig, ax1 = plt.subplots(figsize=(15, 10))

data_labels = ["Number of Users (Millions)","Time Spent (Hours)","Revenue (Billions of Dollars)"]
line_labels = ["Social Networking Sites","Microblogging Sites","Video Sharing Platforms","Photo Sharing Platforms","News Websites","Online Forums","Messaging Apps","Search Engines","E-commerce Websites","Blog Websites","Online Gaming Platforms","Music Streaming Services","Video Streaming Services"]

data = np.array([[2300, 5.5, 40],
                 [1100, 2.3, 15],
                 [1000, 4.2, 25],
                 [800, 3.6, 20],
                 [700, 1.8, 10],
                 [600, 2.2, 5],
                 [550, 3.8, 30],
                 [500, 6.2, 50],
                 [450, 2.9, 35],
                 [400,2.5, 10],
                 [350, 4.5, 40],
                 [300, 3.2, 15],
                 [250, 4.8, 20]])

ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax4 = ax1.twinx()

# plt.gca().set_autoscale_on(False)

ax1.bar(line_labels, data[:, 0], color='darkblue', alpha=0.7, label=data_labels[0])
ax1.set_xticklabels(line_labels, rotation=90)
ax1.set_ylabel(data_labels[0], color='darkblue')
ax1.yaxis.set_major_locator(AutoLocator())

ax2.plot(line_labels, data[:, 1], color='darkorange', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='darkorange')
ax2.yaxis.set_major_locator(AutoLocator())

ax3.scatter(line_labels, data[:, 2], color='darkgreen', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='darkgreen')
ax3.yaxis.set_major_locator(AutoLocator())
ax3.spines["right"].set_position(("axes", 1.1))

ax1.yaxis.label.set_color('darkblue')
ax2.yaxis.label.set_color('darkorange')
ax3.yaxis.label.set_color('darkgreen')
ax1.tick_params(axis='y', colors='darkblue')
ax2.tick_params(axis='y', colors='darkorange')
ax3.tick_params(axis='y', colors='darkgreen')


plt.title('Social Media and the Web: User Engagement, Revenue, and Market Share')
plt.grid(visible=True)
fig.legend(bbox_to_anchor=(1.0, 0.9), loc="upper right")
fig.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/264_202312311430.png', format='png', dpi=300)
plt.clf()
