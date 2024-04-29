
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
data_labels = ["Heritage Preservation","Cultural Exchange","Artistic Performance","Education Outreach","Public Engagement"]
line_labels = ["Category","Ratio"]
data = np.array([[15,22,37,12,14]])

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
wedges, texts = ax.pie(data[0], startangle=90, counterclock=False, wedgeprops=dict(width=0.5), colors=colors)
for i,p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2.0 + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    ax.annotate(data_labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, fontsize=14,
                bbox=dict(boxstyle="round", fc="w"),
                arrowprops=dict(arrowstyle="-", connectionstyle=connectionstyle, color="gray"),
                )
ax.set_title("Arts and Culture Impact in Society - 2023")
centre_circle = plt.Circle((0,0), 0.5, fc='white')
ax.add_artist(centre_circle)
ax.legend(data_labels, loc="center right", bbox_to_anchor=(1.2, 0.5))
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_69.png")
plt.clf()