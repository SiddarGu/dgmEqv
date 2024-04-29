import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

raw_data = """Facebook,2568,34,85.97,3.7
YouTube,2000,40,15.15,5.5
WhatsApp,2000,28,5.12,6.1
Facebook Messenger,1300,12,10.52,2.9
WeChat,1121,66,15.63,0.4
Instagram,1121,28,9.08,2.0
TikTok,689,52,1.0,19.4
Snapchat,433,30,2.21,2.8
LinkedIn,310,17,6.8,1.9
Twitter,330,3.1,3.72,-0.7
Pinterest,322,14,1.69,1.0
Reddit,430,11,2.22,0.4
Tumblr,327,8,0.8,0.2
Viber,260,8,0.21,0.3
Skype,200,15,2.02,0.9"""
data_labels = ['Monthly Active Users (Millions)', 'Average Time Spent Per Day (Minutes)', 
               'Revenue (Billions of Dollars)', 'Yearly Growth (%)']
plot_types = ['bar', 'line', 'scatter', 'fill']
data = np.array([line.split(",")[1:] for line in raw_data.split("\n")]).astype(float)
line_labels = [line.split(",")[0] for line in raw_data.split("\n")]

fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)
axes = [ax1] + [ax1.twinx() for _ in range(data.shape[1] - 1)]
color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

for i in range(data.shape[1]):
    ax = axes[i]
    ax.set_ylabel(data_labels[i], color = color_cycle[i])
    ax.tick_params(axis='y', colors=color_cycle[i])
    if i == 0:
        ax.bar(line_labels, data[:, i], color=color_cycle[i], alpha=0.6)
    elif i == 1:
        ax.plot(line_labels, data[:, i], color=color_cycle[i])
    elif i == 2:
        ax.scatter(line_labels, data[:, i], color=color_cycle[i])
    elif i >= 3:
        ax.fill_between(line_labels, data[:, i], color=color_cycle[i], alpha=0.5)

    if i >= 2:
        ax.spines['right'].set_position(('outward', (i-1)*60))

plt.autoscale(enable=True, axis='x', tight=True)
ax1.set_title('Social Media Analysis: User Engagement, Revenue, and Growth Trends')
ax1.xaxis.grid(True)
ax1.set_xlabel('Platform')
plt.subplots_adjust(right=0.75)
fig.legend(data_labels, loc='upper right', bbox_to_anchor=(1, 0.95))

# Save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/247_202312311051.png')
plt.clf() # Clear the current image state
