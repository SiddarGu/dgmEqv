
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Music', 'Art', 'Theatre', 'Literature', 'Dance'] 
data = [21, 25, 22, 19, 13] 
line_labels = ['Category', 'ratio'] 

fig, ax = plt.subplots(figsize=(10, 10)) 
plt.title('Arts and Culture Performance - 2023') 

cmap = plt.cm.hsv 
inner_circle = plt.Circle((0, 0), 0.70, color='white')

wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40, colors=cmap(np.linspace(0.2, 0.8, len(data)))) 
bbox_props = dict(boxstyle="square, pad = 0.3", fc='white', ec='k', lw=0.72)
kw = dict(arrowprops=dict(arrowstyle='-', color='k'), bbox=bbox_props, zorder=0, va='center') 

for i, p in enumerate(wedges): 
    ang = (p.theta2 - p.theta1)/2. + p.theta1 
    y = np.sin(np.deg2rad(ang)) 
    x = np.cos(np.deg2rad(ang)) 
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))] 
    connectionstyle = 'angle, angleA=0, angleB={}'.format(ang) 
    kw['arrowprops'].update({"connectionstyle": connectionstyle}) 
    ax.annotate(data_labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw) 

ax.legend(data_labels, loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1)) 
ax.add_artist(inner_circle) 

ax.set_facecolor('white') 
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_57.png') 
plt.clf()