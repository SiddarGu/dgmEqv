import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = [
    ["2019", 25000, 4000, 1800],
    ["2020", 23000, 4150, 2000],
    ["2021", 22000, 4300, 2200],
    ["2022", 20000, 4400, 2400],
    ["2023", 19000, 4500, 2600]
]

# Separate the data into x_values (years), y_values (metrics), and data (values)
x_values = np.array([x[0] for x in data], dtype=str)
y_values = np.array(["Carbon Dioxide Emissions (Kilotonnes)", "Forestation Area (Million Hectares)", "Renewable Energy Consumption (Million MWh)"])
data = np.array([x[1:] for x in data], dtype=np.float32)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

width = depth = 0.7
for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), width, depth, data[:, i], alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=90)
ax.set_yticklabels(y_values, ha='left')
ax.set_zlim(bottom=0)  # Ensure bars start at 0
ax.view_init(azim=165)  # Adjust viewing angle
plt.title("Sustainability Metrics: CO2 Emissions, Forestation, and Renewable Energy Consumption (2019-2023)")
plt.grid(True)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/256_202312310050.png")
plt.clf()
