import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_values = ['USA', 'UK', 'France', 'Spain', 'Italy']
y_values = ['Number of Tourists (Millions)', 'Average Spending per Tourist ($)', 'Total Revenue from Tourism ($Billions)']
data = np.array([[15,20,30], [10,15,15], [12,18,21.6], [8,14,11.2], [11,16,17.6]])

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
yticks = [i for i in range(len(y_values))]
for c, k in zip(colors, yticks):
    xs = np.arange(len(x_values))
    ys = data[:, k]
    
    # You can provide either a single color or an array with the same length as xs and ys.
    cs = [c]*len(xs)
    
    # Plot bars
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('Country')
ax.set_ylabel('Metrics')
ax.set_zlabel('Values')
ax.set_xticks(xs)
ax.set_yticks(yticks)
ax.set_xticklabels(x_values, rotation=45, horizontalalignment="right")
ax.set_yticklabels(y_values)
plt.title('International Tourism and Hospitality Revenue Analysis by Country')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/81_202312302126.png')

# clear the current figure
plt.clf()
