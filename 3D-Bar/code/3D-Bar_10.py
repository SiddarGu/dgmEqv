
import matplotlib.pyplot as plt
import numpy as np

y_values = ["Facebook Users (million)", "Twitter Users (million)", "Instagram Users (million)", "Youtube Users (million)"]
data = np.array([[1.5, 0.3, 0.8, 1.5],
                 [2.0, 0.4, 1.2, 2.0],
                 [2.5, 0.5, 1.6, 2.5],
                 [3.0, 0.6, 2.0, 3.0],
                 [3.5, 0.7, 2.4, 3.5]])
x_values = ["2015", "2016", "2017", "2018", "2019"]

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs,ys,[0] * len(xs), dx=0.3, dy=0.3, dz=data[:,i], color=plt.cm.Set1(i/len(y_values)), alpha=0.8)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_title("Popular Social Media Platforms User Trends - 2015 to 2019")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/4_202312270030.png')
plt.clf()