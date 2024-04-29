
import matplotlib.pyplot as plt
import numpy as np

y_values = ["Coal Production (Million Tonnes)", "Wind Energy Output (GWh)", "Hydro Energy Output (GWh)", "Solar Energy Output (GWh)"]
data = np.array([[50,500,600,700],[60,400,500,800],[45,480,650,750],[55,460,720,850]])
x_values = ["North", "South", "East", "West"]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')

width, depth, colors, alpha = 0.5, 0.5, ['b','g','r','c'], 0.7

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ax.bar3d(xs, [i]*len(x_values), np.zeros(len(x_values)), width, depth, data[:,i], color=colors[i], alpha=alpha)

ax.set_title("Regional Energy Trends - Coal, Wind, Hydro and Solar Outputs")
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/25_202312251036.png")
plt.clf()