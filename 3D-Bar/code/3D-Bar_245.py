
import numpy as np
import matplotlib.pyplot as plt

y_values=['Housing Starts (Units)','Average Home Value ($000)','Number of Listings']
x_values=['North','South','East','West']
data=np.array([[50,200,100],[30,150,200],[45,80,180],[55,60,150]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:,i], shade=True, color='g')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Real Estate Market Insights by Region')

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/5_202312251044.png")
plt.clf()