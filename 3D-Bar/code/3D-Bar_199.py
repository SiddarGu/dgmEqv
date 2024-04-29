import matplotlib.pyplot as plt
import numpy as np

data_string = "Year,Coal Production (Million Tonnes),Natural Gas Production (Billion Cubic Meters),Nuclear Energy Production (GWh),Renewable Energy Production (GWh)\n 2019,20,80,150,180\n 2020,22,85,155,190\n 2021,24,90,160,200\n 2022,25,110,180,220\n 2023,27,115,185,240"
data_lines = data_string.split('\n')

# Parsing Data
headers = data_lines[0].split(',')
y_values = headers[1:]
x_values = [line.split(',')[0] for line in data_lines[1:]]
data = np.array([list(map(np.float32, line.split(',')[1:])) for line in data_lines[1:]])

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

x_pos = np.arange(len(x_values))

for i in range(len(y_values)):
    ax.bar(x_pos, data[:, i], i, zdir='y', color='b', alpha=0.8)

ax.set_title("Energy Production Types Trends: 2019-2023")

ax.set_xticks(x_pos)
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/112_202312302126.png")
plt.clf()
