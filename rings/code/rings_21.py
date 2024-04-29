
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Ticket Sales', 'Broadcasting Rights', 'Marketing', 'Sponsorship', 'Merchandise']
data = [30, 25, 15, 20, 10]
line_labels = ['Category', 'ratio']

fig=plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111)
wedges, texts, autotexts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40, counterclock=False,
                                 autopct=lambda pct: '{:.1f}%'.format(pct))

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(data_labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.set_title('Sports and Entertainment Revenue - 2023')
ax.legend(data_labels, loc="upper right", bbox_to_anchor=(1.2, 0.95))
ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_32.png')
plt.clf()