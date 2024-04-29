
import matplotlib.pyplot as plt
import numpy as np

data = ['Convenience Foods','Fresh Foods','Natural and Organic Foods','Processed Foods','Functional Foods']
percentage = [25,20,30,15,10]

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(5)*4)
wedges, texts, autotexts = ax.pie(percentage, autopct='%1.1f%%', pctdistance=0.8,
        shadow=True, startangle=90, colors=outer_colors,
        textprops=dict(color="k", fontsize=15, va="center"))

ax.set_title("Distribution of Food and Beverage Products in the US, 2023", fontsize=18)
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
        bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontal_alignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(data[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontal_alignment, **kw)

ax.set_xticks([])
ax.set_yticks([])
plt.tight_layout()
plt.savefig('pie chart/png/18.png')
plt.clf()