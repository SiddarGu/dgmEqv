
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Renewable Energy','Energy Efficiency','Power Grid Reliability','Cost Management']
data = np.array([44,27,15,14])
line_labels = ['Category']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
wedges, texts = ax.pie(data, startangle=90, counterclock=False, wedgeprops=dict(width=0.3))
ax.set_title('Energy and Utilities Performance - 2023')
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = f"angle,angleA=0,angleB={ang},rad=10"
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(data_labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                 horizontalalignment=horizontalalignment, **kw)

center = plt.Circle((0, 0), 0.35, color='white')
ax.add_artist(center)
ax.legend(data_labels)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_76.png', dpi=300)
plt.cla()