
import numpy as np
import matplotlib.pyplot as plt

y_values = ["Life Expectancy (Years)", "GDP per Capita (USD)", "Unemployment Rate (%)"]
data = np.array([[79.2, 40, 38], [81.1, 40, 52], [84.4, 30, 24], [76.3, 40, 24], [69.6, 10, 62]])
x_values = ["USA", "Germany", "Japan", "China", "India"]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    zs = data[:, i]
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, zs, alpha=0.3 * (i + 1), color=plt.cm.Set1(i))
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_title("Social Sciences and Humanities Trends Across Countries")
fig.tight_layout()
fig.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/4_202312251000.png")
plt.clf()