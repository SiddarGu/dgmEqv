import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

# data
raw_data = '''Category,Number of Users (Millions),Number of Posts (Millions),Engagement Rate (%),Click Through Rate (%)
Facebook,2500,3500,50,10
Instagram,1000,4500,60,8
Twitter,500,2500,40,5
YouTube,2000,5000,70,12
LinkedIn,400,1500,30,4
Snapchat,800,3000,55,7
Pinterest,600,2000,45,6
TikTok,1200,4000,65,9
WhatsApp,1500,3500,60,11
WeChat,700,2800,50,7'''

# transforming data
raw_data = raw_data.split('\n')
line_labels = [line.split(',')[0] for line in raw_data[1:]]
data_labels = raw_data[0].split(',')[1:]
data = np.array([list(map(int, line.split(',')[1:])) for line in raw_data[1:]])

# colors, alphas and plot types
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '0.5', '0.3']
alphas = [1, 0.75, 0.5, 0.25]
plot_types = ['bar', 'line', 'line', 'line']

# figure
fig, ax1 = plt.subplots(figsize=(22, 15))
x = np.arange(len(data))

def plot_data(ax, data, plot_type, color, alpha=1):
    if plot_type == 'bar':
        return ax.bar(x, data, color=color, alpha=alpha)
    elif plot_type == 'line':
        return ax.plot(x, data, color=color, linewidth=2)
    elif plot_type == 'area':
        return ax.fill_between(x, data, color=color, alpha=alpha)

ax2, ax3, ax4 = ax1.twinx(), ax1.twinx(), ax1.twinx()
axes = [ax1, ax2, ax3, ax4]
for ax, data_sub, data_label, plot_type, color, alpha in zip(axes, data.T, data_labels, plot_types, colors, alphas):
    p = plot_data(ax, data_sub, plot_type, color, alpha)
    ax.set_ylabel(data_label, color=color)
    ax.tick_params(axis='y', colors=color)
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    plt.legend(p, [data_label], loc='upper left')

# the position of ax3, ax4
for ax in [ax3, ax4]:
    ax.spines['right'].set_position(('outward', 60*(axes.index(ax)-1)))

plt.title("Performance Comparison of Social Media Platforms")
plt.xticks(x, line_labels, rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/318_202312311430.png")
plt.cla()
