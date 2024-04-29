
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[300,450,250],[500,350,400],[250,400,500],[150,200,100]])
y_values = ['Number of Criminal Cases','Number of Civil Cases','Number of Regulatory Cases']
x_values = ['State','Federal','International','Other']

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    width = depth = 1
    colors = plt.cm.plasma(data[:,i]/float(data.max()))
    ax.bar3d(xs, ys, np.zeros(len(x_values)), width, depth, data[:,i], shade=True, color=colors, alpha=1)

ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values)
ax.xaxis.set_tick_params(rotation=90)

plt.title('Global Law & Legal Cases Overview - Distribution by Area')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/27_202312251036.png')
plt.clf()