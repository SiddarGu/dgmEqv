
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

y_values = ['Number of Cases','Average Duration (Days)','Average Cost ($)']
x_values = ['Civil Disputes','Criminal Charges','Family Law','Immigration Law']
data = np.array([[200,150,100],[150,180,150],[100,90,75],[50,60,80]])

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:,i], alpha=0.6, color=['b','r','g','y'], shade=True)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, rotation=60)
ax.view_init(15, 30)
ax.set_title('Overview of Law and Legal Affairs Cases - Number, Duration and Cost')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/43_202312270030.png')
plt.clf()