import matplotlib.pyplot as plt
import numpy as np

data = np.array([[300, 450, 20], [550, 800, 30], [800, 1200, 50], [1000, 1500, 70]])
y_values = ["Number of Regular Check-ups","Average Healthcare Spending ($)","Prevalence of Chronic Diseases (%)"]
x_values = ['18-29', '30-49', '50-64', '65+']

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['blue', 'green', 'red']
yticks = np.arange(3)

for c, k in zip(colors, yticks):
    xs = np.arange(len(x_values))
    ys = data[:, k]

    # You can provide either a single color or an array with the same length as
    # x and y. To demonstrate this, we color the first bar of each set cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'

    # Plot bars.
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('Age Group')
ax.set_ylabel('Metrics')
ax.set_zlabel('Values')

# On the y axis let's interval the labels
ax.set_yticks(yticks)
ax.set_yticklabels(y_values, ha='left')

# On the x axis let's interval the labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')

ax.set_title('Healthcare Utilization and Spending by Age Group')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/189_202312302235.png')
plt.clf()
