import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Parse data
rows = '''Platform, Monthly Active Users (Millions), Average Time Spent (Minutes), Ad Revenue (Billions)
 Facebook, 2745, 58.5, 84.17
 YouTube, 2000, 40.9, 15.15
 WhatsApp, 2000, 28.4, 5.0
 Facebook Messenger, 1300, 10.6, 1.27
 WeChat, 1200, 66.4, 6.18
 Instagram, 1121, 28.0, 20.0
 TikTok, 689, 52.0, 1.0
 Reddit, 430, 37.8, 0.1
 Twitter, 353, 3.1, 3.46
 Snapchat, 293, 30.0, 2.5'''.split('\n')
df = pd.DataFrame([row.split(',') for row in rows[1:]], columns=rows[0].split(',')).astype({' Monthly Active Users (Millions)': int,
                                                                                             ' Average Time Spent (Minutes)' : float,
                                                                                             ' Ad Revenue (Billions)'       : float})

# Plotting
colors = ['b', 'g', 'r']
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
df.plot(x='Platform', y=' Monthly Active Users (Millions)', kind='bar', ax=ax, color=colors[0], position=1, label='Monthly Active Users (Millions)')
ax2 = ax.twinx()
df.plot(x='Platform', y=' Average Time Spent (Minutes)', kind='line', ax=ax2, color=colors[1], label='Average Time Spent (Minutes)')
ax3 = ax.twinx()
df.plot(x='Platform', y=' Ad Revenue (Billions)', kind='line', ax=ax3, color=colors[2], label='Ad Revenue (Billions)')

ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel('Ad Revenue (Billions)')
ax3.yaxis.label.set_color(colors[2])

ax.set_ylabel('Monthly Active Users (Millions)')
ax.yaxis.label.set_color(colors[0])
ax2.set_ylabel('Average Time Spent (Minutes)')
ax2.yaxis.label.set_color(colors[1])

handles,labels = [],[]
for ax in fig.axes:
    for h,l in zip(*ax.get_legend_handles_labels()):
        handles.append(h)
        labels.append(l)

plt.title('User Statistics and Ad Revenue: A Comparison of Social Media Platforms')
plt.grid(True)
plt.legend(handles,labels,loc='best')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/Full/multi-axes/png_train/multi-axes_192.png')
plt.close()
