
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data_labels = ["Subscribers (Thousands)", "Revenue (Millions of Dollars)", "Average View Count"]
line_labels = ["Podcasts", "Social Media", "Books", "Audio-Books", "Magazines", "Newspapers", "Video Streaming", "Music Streaming"]

data = np.array([[98, 1750, 128], [1230, 3300, 140], [290, 1450, 670], [400, 1700, 600], [280, 1300, 570], [320, 1020, 470], [990, 2050, 260], [1150, 3500, 120]])

fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:,0], label=data_labels[0], width=0.2, color='#ff9900', alpha=0.6)
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], label=data_labels[1], marker='o', color='#0099ff')
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.plot(line_labels, data[:,2], label=data_labels[2], marker='^', color='#33cc33')

ax1.set_xlabel('Category', fontsize=14)
ax1.set_ylabel(data_labels[0], fontsize=14, color='#ff9900')
ax2.set_ylabel(data_labels[1], fontsize=14, color='#0099ff')
ax3.set_ylabel(data_labels[2], fontsize=14, color='#33cc33')

ax1.tick_params(axis='y', labelcolor='#ff9900')
ax2.tick_params(axis='y', labelcolor='#0099ff')
ax3.tick_params(axis='y', labelcolor='#33cc33')

ax1.set_title("Social Sciences and Humanities Subscription Services Performance", fontsize=20)

ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

ax1.grid()

for ax in [ax1, ax2, ax3]:
    ax.xaxis.set_major_locator(ticker.AutoLocator())
    ax.yaxis.set_major_locator(ticker.AutoLocator())

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/50_2023122270030.png")
plt.clf()